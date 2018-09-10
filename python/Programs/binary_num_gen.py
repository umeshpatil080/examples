class BinaryGen():
    def __init__(self):
        self.queue = []
        self.i = 0
        self.j = 0
        self.queue.append('1')

    def _pop_queue_item(self):
        if(self.i <= self.j):
            item = self.queue[self.i]
            self.i = self.i + 1
            return item
        else:
            raise Exception("Queue is empty")

    def _add_item_to_queue(self, item):
        self.queue.append(item)
        self.j = self.j + 1

    def generate_binary_sequence_upto(self, n):
        binary_nums = []
        while(n > 0):
            item = self._pop_queue_item()
            binary_nums.append(item)
            n -= 1
            push_item1 = item + '0'
            push_item2 = item + '1'
            self._add_item_to_queue(push_item1)
            self._add_item_to_queue((push_item2))

        return binary_nums

if(__name__ == '__main__'):
    b_num = BinaryGen()
    n = 10
    binary_nums = b_num.generate_binary_sequence_upto(n)
    print(binary_nums)

