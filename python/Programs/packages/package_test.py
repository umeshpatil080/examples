#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     14/10/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from package1 import *  # 'import *' loads only modules listed in '__all__' list in module 'package1/__init__.py'
                        # Other modules can be loaded by explicit import like 'from package1 import module2'

from package1.package2 import module1 as p1_p2_m1

def main():
    module1.info()
    try:
        module2.info() # "package1.module2" is not loaded as 'package1/__init__.py' has '__all__ = ['module1']'
    except:
        print("Issue loading 'package1.module2'")

    from package1 import module2 # Explicit import makes '__all__' list in 'package1/__init__.py' ineffective
    module2.info()

    p1_p2_m1.info()
if __name__ == '__main__':
    main()
