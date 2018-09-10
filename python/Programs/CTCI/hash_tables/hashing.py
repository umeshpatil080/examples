import sys

from single_linked_list import SingleLinkedList


HASH_TABLE_SIZE = 599

class HashTable():
    def __init__(self, size):
        self._size = size
        self._hash_table = [None,] * self._size

    def _get_hash_key(self, key):
        if(key):
            sum =0
            for ch in key:
                sum += ord(ch)
            hash_key = sum % self._size
            return hash_key
        else:
            raise Exception("Key cannot be None")

    def add(self, key, value):
        index = self._get_hash_key(key)
        if(self._hash_table[index]):
            # Need to check for duplicate keys
            #  Overwrite value for existing key
            self._hash_table[index].add_rear(key, value)
        else:
            hash_bucket = SingleLinkedList()
            hash_bucket.add_rear(key, value)
            self._hash_table[index] = hash_bucket

    def get(self, key):
        index = self._get_hash_key(key)
        if(self._hash_table[index]):
            bucket_root = self._hash_table[index].root
            while(bucket_root):
                if(bucket_root.key == key):
                    return bucket_root.value
                bucket_root = bucket_root.next
            return None
        else:
            return None

    def print_hash_table(self):
        for hash_bucket in self._hash_table:
            if(hash_bucket):
                hash_bucket.print()
                sys.stdout.write("\n")


def main():
    data = "abcd"
    ht = HashTable(HASH_TABLE_SIZE)
    ht.add("one", data)
    ht.add("two", data)
    ht.add("two", data)
    ht.add("three", "xyz")
    ht.print_hash_table()

    key = "three"
    value = ht.get(key)
    print("{0} => {1}".format(key, value))

if __name__ == '__main__':
    main()
