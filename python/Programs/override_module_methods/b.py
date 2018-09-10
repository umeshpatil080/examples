from a import *
import a

def foo():
   print ("This was foo:")
   a.foo()
   print ("But it was overridden.")