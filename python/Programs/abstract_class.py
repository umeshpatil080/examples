import asyncio
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def sam(self):
        pass

class ChildClass(AbstractClass):
    def __init__(self):
        pass

    def sam(self):
        print("In ChildClass sam\n")

def main():
    a = ChildClass()
    a.sam()


if __name__ == '__main__':
    main()
