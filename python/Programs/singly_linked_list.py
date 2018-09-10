#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     17/09/2017
# Copyright:   (c) pumesh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node

class SingleLinkedList:
    def __init__(self):
        self.root = None

    def add_rear(self, data):
        node = Node(data, None)
        cur = self.root
        if(cur == None):
            self.root = node
            return

        while(cur.next != None):
            cur = cur.next
        cur.next = node

    def add_front(self, data):
        node = Node(data)
        if(self.root == None):
            self.root = node
            return
        else:
            root = self.root
            node.next = root
            self.root = node

    def delete_rear(self):
        cur = self.root
        prev = None
        if(cur != None):
            if(cur.next == None):
                return cur
                self.root = None
            else:
                while(cur.next != None):
                    prev = cur
                    cur = cur.next
                prev.next = None
                return cur

    def delete_front(self):
        root = self.root
        if(self.root != None):
            self.root = root.next
        return root

    def print_list(self):
        cur = self.root
        while(cur != None):
            sys.stdout.write("->%s" % str(cur.data))
            cur = cur.next
        print("")

def main():
    s_list = SingleLinkedList()
    print("At start")
    s_list.print_list()

    print("Adding rear 1")
    s_list.add_rear(1)
    s_list.print_list()

    print("adding rear 2")
    s_list.add_rear(2)
    s_list.print_list()

    print("Adding front 0")
    s_list.add_front(0)
    s_list.print_list()

    print("\ndeleting rear")
    node = s_list.delete_rear()
    print("deleted:%s" % str(node.data))
    s_list.print_list()

    print("\ndeleting front")
    node = s_list.delete_front()
    print("deleted:%s" % str(node.data))
    s_list.print_list()

if __name__ == '__main__':
    main()