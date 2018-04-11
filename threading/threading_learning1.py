# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:14:05 2018

@author: busby
"""

import threading

def thread_job():
    print("This is an added Thread, number is %s" % threading.current_thread())

def main():
    added_thread = threading.Thread(target = thread_job)
    added_thread.start()
    
    #print(threading.active_count())
    #print(threading.enumerate())
    #print(threading.current_thread())
    

if __name__ == '__main__':
    main()