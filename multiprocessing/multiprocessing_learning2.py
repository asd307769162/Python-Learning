# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:08:50 2018

@author: busby
"""

import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(10000000):
        res += i+i**2+i**3
    q.put(res)

def normal():
    res = 0
    for _ in range(2):
        for i in range(10000000):
            res += i+i**2+i**3
    print("normal:",res)

def multiprocessing():
    q = mp.Queue()
    p1 = mp.Process(target = job, args = (q,))
    p2 = mp.Process(target = job, args = (q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print("multicore:",res1+res2)
    
def multithread():
    q = mp.Queue()
    t1 = td.Thread(target = job, args = (q,))
    t2 = td.Thread(target = job, args = (q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print("multithread",res1+res2)
    
if __name__ == '__main__':
        
    st01 = time.time()
    normal()
    st1 = time.time()-st01
    print("normal time:",st1)
    
    st02 = time.time()
    multiprocessing()
    st2 = time.time()-st02
    print("multiprocessing time:",st2)
    
    st03 = time.time()
    multithread()
    st3 = time.time()-st03
    print("multithread time:",st3)

