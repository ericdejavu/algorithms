# -*- coding:utf8 -*-
from lru import LRU
from lfu import LFU
import time

def testLRU():
    lru = LRU(5)
    for i in range(8):
        lru.put(str(i), i)
        if i == 5:
            lru.get(str(i))
    lru.remove('3')
    lru.showNodes()

def testLFU():
    lfu = LFU(5)
    for i in range(8):
        print (i)
        lfu.put(str(i), i)
        time.sleep(0.1)
        if i == 5:
            lfu.get(str(i))
            for j in range(3):
                lfu.get(str(i))
        if i == 2:
            lfu.get(str(i))
    lfu.remove('2')

    lfu.showNodes()


# testLRU()
testLFU()