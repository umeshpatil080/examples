import sys

class SingleLinkedList():
    def __init__(self):
        self.root = None

    class Node():
        def __init__(self, key, value, next = None):
            self.key = key
            self.value = value
            self.next = next

    def add_front(self, key, value):
        return self._add_front(self.Node(key, value))

    def _add_front(self, node):
        if(self.root):
            node.next = self.root
            self.root = node
        else:
            self.root = node

    def add_rear(self, key, value):
        return self._add_rear(self.Node(key, value))

    def _add_rear(self, node):
        if(self.root is None):
            self.root = node
        else:
            temp = self.root
            while(temp.next):
                temp = temp.next
            temp.next = node

    def print(self):
        temp = self.root
        while(temp):
          sys.stdout.write("=>[{0}:{1}]".format(temp.key, temp.value))
          temp = temp.next


def main():
    sList = SingleLinkedList()

    sList.add_front("one", 1)
    sList.add_rear("two", 2)
    sList.add_front("zero", 0)

    sList.print()

if __name__ == '__main__':
    main()
