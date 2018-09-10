#-------------------------------------------------------------------------------
# Name:        __init__.py
# Purpose:
#
# Author:      pumesh
#
# Created:     14/10/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
__init__.py - instructs python to consider directory in which it is present to onsider as a package.

__init__.py file ideally does not need to contain any code. If required initialization code can be place in it.

'__all__' list can be defined to make the modules defined in this package to be available via this package.


"""

print("In __init__.py")

"""
In case 'from package1 import *' is used in other module/script then, only "module1" will be available as "__all__" list has entry for only "module1".

"__all__" is effective case when "import *" is used.

"module2" will still be accessible if explicit import like "from package1 import module2" is used

"""
__all__ = ['module1']
