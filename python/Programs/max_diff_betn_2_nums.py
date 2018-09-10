"""
Maximum diference between two elements such that larger element appears after
the smaller number

"""

class MaxDiffNumbers():
    def __init__(self):
        pass

    def get_max_diff_betn_2_nums(self, lst):
        if(not lst):
            raise Exception("List cannot be empty.")
        else:
            i = 0
            min_num = max_num = lst[i]
            max_diff = max_num - min_num

            for x in lst:
                if((x - min_num) > max_diff):
                    max_diff = x - min_num
                    max_num = x
                    if(x < min_num):
                        min_num = x

            print("Max num:{0}\nMin num:{1}".format(max_num, min_num))
            return max_diff


def main():
    lst1 = [7, 9, 5, 6, 3, 2]
    obj1 = MaxDiffNumbers()
    res = obj1.get_max_diff_betn_2_nums(lst1)
    print("Max diff between 2 elements in {1} is: {0}\n".format(res, lst1))

    lst2 = [2, 3, 10, 6, 4, 8, 1]
    res = obj1.get_max_diff_betn_2_nums(lst2)
    print("Max diff between 2 elements in {1} is: {0}\n".format(res, lst2))

if __name__ == '__main__':
    main()
