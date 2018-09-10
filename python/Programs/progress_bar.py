#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     09/11/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
import sys


def main():
   for progress in range(100):
      time.sleep(0.1)
      sys.stdout.write("Download progress: %d%%   \r" % (progress) )
      sys.stdout.flush()

if __name__ == '__main__':
    main()
