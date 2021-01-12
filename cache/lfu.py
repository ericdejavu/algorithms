# -*- encoding: utf8 -*-
import time

class LFU:

    ## public

    def __init__(self, capacity = 2):
        # write and lfu
        self.head = None
        self.tail = None
        # read
        self.map = {}
        if capacity <= 1:
            raise ValueError('LFU capacity must large than 1')
        self.capacity = capacity

    def put(self, key, value):
        if not key or key == '':
            return
        node = self.map.get(key)
        if not node:
            if len(self.map) >= self.capacity:
                tmp = self.head
                self.__evict(self.head)
                self.map.pop(tmp.key)
                tmp.destory()
            node = LFU.__ADNode(key, value)
            self.map[key] = node
            self.__add(node, self.head)
        else:
            node.data = value

    def get(self, key):
        if not key or key == '':
            return
        node = self.map.get(key)
        if node:
            self.__update(node)
            return node.data

    def remove(self, key):
        if not key or key == '':
            return
        node = self.map.get(key)
        if node:
            self.__evict(node)
            self.map.pop(key)
            node.destory()
    
    # debug only
    def showNodes(self):
        print ('dict:', self.map)
        node = self.head
        while node:
            print (node.key, node._cnt, node._time)
            node = node.next

    ## private

    # A generic doubly linked node
    class __ADNode:
        def __init__(self, key=None, data=None):
            self.data = data
            self.key = key
            self._time = time.time()
            self._cnt = 0
            self.pre = None
            self.next = None

        def hit(self):
            self._time = time.time()
            # cant handle high freq sence
            self._cnt += 1

        def detach(self):
            self.pre = None
            self.next = None

        def destory(self):
            self.detach()
            self.key = None
            self.data = None
            self._time = None
            self._cnt = None

        def moreFreqThan(self, node):
            if not node:
                return
            if self._cnt != node._cnt:
                return self._cnt > node._cnt
            
            return self._time > node._time
            
    def __locate(self, start, node):
        if not start:
            raise ValueError('start must not be null')
        cur = start
        while cur:
            if cur.moreFreqThan(node):
                break
            cur = cur.next
            # dead loop
            if cur == node:
                raise RuntimeError('ring list appeared')
        return cur

    def __add(self, node, anchor):
        if self.head and self.tail:
            cur = self.__locate(anchor, node)
            if node == cur:
                return
            # large than tail
            if not cur:
                node.pre = self.tail
                node.next = None
                self.tail.next = node
                self.tail = node
            else:
                node.next = cur
                node.pre = cur.pre
                cur.pre.next = node
                cur.pre = node

        if not self.head:
            self.head = node
        elif not self.tail:
            self.tail = node
            self.head.next = node
            self.head.pre = None
            node.pre = self.head
            node.next = None
        

    def __evict(self, node):
        if not node:
            return
        if node == self.tail:
            self.tail = self.tail.pre
            self.tail.next = None
        elif node == self.head:
            self.head = self.head.next
            self.head.pre = None
        else:
            node.pre.next = node.next
            node.next.pre = node.pre

    def __moveNode(self, anchor, node):
        if anchor == node:
            return
        elif node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            return
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        
        if not anchor:
            node.next = None
            node.pre = self.tail
            self.tail.next = node
            self.tail = node
        else:
            node.next = anchor
            node.pre = anchor.pre
            anchor.pre.next = node
            anchor.pre = node


    # update list by 
    def __update(self, node):
        if not node:
            return
        node.hit()
        if node == self.tail:
            return
        cur = self.__locate(node.next, node)
        if not cur:
            self.__moveNode(None, node)
            return
        self.__moveNode(cur, node)