# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:20:37 2018

@author: busby
"""


import threading
import time

def thread_job():
    print("T1 start \n")
    for i in range(10):
       time.sleep(0.1) 
    print("T1 finish \n")
    
def T2_job():
    print("T2 start \n")
    print("T2 finish \n")
    
def main():
    added_thread = threading.Thread(target = thread_job, name = 'T1')
    thread2 = threading.Thread(target = T2_job, name = 'T2')
    added_thread.start()
    thread2.start()
    added_thread.join()
    thread2.join()
    print('all done \n')
    
    #print(threading.active_count())
    #print(threading.enumerate())
    #print(threading.current_thread())
    

if __name__ == '__main__':
    main()