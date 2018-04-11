# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 21:10:58 2018

@author: busby
"""

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    #pool = mp.Pool() 使用全部核心
    pool = mp.Pool(processes = 2)
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job,(1000,))
    print(res.get())
    multi_res =[pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multicore()