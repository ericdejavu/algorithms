# -*- encoding: utf8 -*-

## O(1)
class LRU:

    ## public

    def __init__(self, capacity = 2):
        # write and lru
        self.head = None
        self.tail = None
        # read
        self.map = {}
        if capacity <= 1:
            raise ValueError('LRU capacity must large than 1')
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
            node = LRU.__ADNode(key, value)
            self.map[key] = node
            self.__add(node)
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
            print (node.key)
            node = node.next

    ## private

    # A generic doubly linked node
    class __ADNode:
        def __init__(self, key=None, data=None):
            self.data = data
            self.key = key
            self.pre = None
            self.next = None

        def detach(self):
            self.pre = None
            self.next = None

        def destory(self):
            self.detach()
            self.data = None

    def __add(self, node):
        if self.tail:
            self.tail.next = node
            node.pre = self.tail
            node.next = None
        self.tail = node
        if self.head == None:
            self.head = node

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

    # update list by 
    def __update(self, node):
        if not node:
            return
        self.__evict(node)
        self.__add(node)