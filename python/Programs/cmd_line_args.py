import os
import sys

def env_vars():
    for a in os.environ:
        print("Var:{0} Value:{1}".format(a, os.environ.get('NODES', None)))

def set_params(param_keys = None):
    if param_keys:
        keys = param_keys.split('~')
        print("keys:")
        print(keys)

def main():
    i = 0
    """
    for arg in sys.argv:
        print("Arg num:{0}\tValue:{1}".format(i, sys.argv[i]))
        i = i + 1
    """
    set_params("a~b")

if __name__ == '__main__':
    #main()
    var1 = input("One:")
    print(var1)
    var2 = input("two:")
    print(var2)
