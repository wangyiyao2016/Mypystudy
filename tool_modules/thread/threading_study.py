'''
Created on Nov 20, 2016

@author: jack
'''

import threading
import time


def thread_job():
    print("thread_job start")
    time.sleep(8)
    print("thread_job done")

def main():
#     print threading.active_count()
#     print threading.enumerate()
#     print threading.current_thread()
    addT = threading.Thread(target=thread_job, name="T1")
    addT.start()
    addT.join()
    
if __name__ == '__main__':
    main()
    pass