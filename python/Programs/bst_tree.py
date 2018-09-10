import sys

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def add_data(self, data):
        node = Node(data = data)

        if(self.root is None):
            self.root = node
        else:
            cur = self.root
            prev = None
            while(cur):
                prev = cur
                if(data < cur.data):
                    cur = cur.left
                else:
                    cur = cur.right

            if(data < prev.data):
                prev.left = node
            else:
                prev.right = node

    def print_tree(self):
        root = self.root
        print("Tree inorder traversal")
        self._print_tree_inorder(root)
        print("\n")

    def _print_tree_inorder(self, node):
        while(node):
            self._print_tree_inorder(node.left)
            sys.stdout.write("{0}\t".format(node.data))
            self._print_tree_inorder(node.right)
            return

    def print_tree_level_order(self):
        """ Level order traveersal of BST tree
        """
        if(self.root is None):
            print("Tree is empty")
            return
        else:
            print("Tree level order traversal")
            cur = self.root
            q = [cur]
            while(q):
                node = q.pop(0)
                sys.stdout.write("{0}\t".format(node.data))

                if(node.left):
                    q.append(node.left)

                if(node.right):
                    q.append(node.right)

    def mirror_tree(self):
        root = self.root
        self._mirror_tree(root)

    def _mirror_tree(self, root):
        if(root is None):
            return
        else:
            self._mirror_tree(root.left)
            self._mirror_tree(root.right)

            # swap lef and right sub tree nodes
            tmp = root.left
            root.left = root.right
            root.right = tmp

            return

def main():
    bst = BST()

    nodes_set1 = (5, 4, 6, 3, 2, 1)
    nodes_set2 = (4, 2, 5, 1, 3)
    for n in nodes_set1:
        bst.add_data(n)

    bst.print_tree()
    bst.print_tree_level_order()
    bst.mirror_tree()
    print("\nAfter mirroring\n")
    bst.print_tree()
    bst.print_tree_level_order()
if __name__ == '__main__':
    main()
