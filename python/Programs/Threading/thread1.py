#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     20/08/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import threading
import logging

def worker(num, str1):
    """ Thread worker function """
    logging.debug("Starting")
    print ("Thread num: %d\tstr:%s\n" % (num, str1))
    logging.debug("Exiting")
    return

def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target = worker, args =(i, "argument to the  thread"))
        threads.append(t)
    for t in threads:
        t.start()

if __name__ == '__main__':
    main()
