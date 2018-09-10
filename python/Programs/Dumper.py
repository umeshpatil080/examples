#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     05/08/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pprint

def printStruct(struc, indent=0):
  if isinstance(struc, dict):
    print '  '*indent+'{'
    for key,val in struc.iteritems():
      if isinstance(val, (dict, list, tuple)):
        print '  '*(indent+1) + str(key) + '=> '
        printStruct(val, indent+2)
      else:
        print '  '*(indent+1) + str(key) + '=> ' + str(val)
    print '  '*indent+'}'
  elif isinstance(struc, list):
    print '  '*indent + '['
    for item in struc:
      printStruct(item, indent+1)
    print '  '*indent + ']'
  elif isinstance(struc, tuple):
    print '  '*indent + '('
    for item in struc:
      printStruct(item, indent+1)
    print '  '*indent + ')'
  else: print '  '*indent + str(struc)


def main():
    d = [{'a1':1, 'a2':2, 'a3':3}, [1,2,3], [{'b1':1, 'b2':2}, {'c1':1}], 'd1', 'd2', 'd3']
    printStruct(d, indent = 4)


if __name__ == '__main__':
    main()
