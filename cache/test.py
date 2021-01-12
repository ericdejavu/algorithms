# -*- coding:utf8 -*-
from lru import LRU
from lfu import LFU
import time

def testLRU():
    print ('######### LRU ########\n')
    lru = LRU(5)
    for i in range(8):
        lru.put(str(i), i)
        if i == 5:
            lru.get(str(i))
    lru.remove('3')
    lru.showNodes()

def testLFU():
    print ('######### LFU ########\n')
    lfu = LFU(5)
    for i in range(8):
        lfu.put(str(i), i)
        time.sleep(0.01)
        if i == 5:
            lfu.get(str(i))
            for j in range(3):
                lfu.get(str(i))
        if i == 2:
            lfu.get(str(i))
    for j in range(5):
        lfu.get('4')
    lfu.remove('2')

    lfu.showNodes()


testLRU()
testLFU()