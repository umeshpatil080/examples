#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      pumesh
#
# Created:     26/01/2018
# Copyright:   (c) pumesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class LIS():
    def __init__(self):
        pass

    def lis(self, num_list):
        if(num_list is not None and len(num_list) > 0):
            i = 1
            j = 0
            lis = [1] * (len(num_list))
            max_lis = 1
            for i in range(len(num_list)):
                for j in range(i):
                    if(num_list[j] < num_list[i] and lis[i] < (lis[j] + 1)):
                        lis[i] = lis[j] + 1
                        if(lis[i] > max_lis):
                            max_lis = lis[i]
        else:
            max_lis = 1

        i = len(lis) - 1
        lis_items = []
        last_max_lis = max_lis
        while(i >= 0):
            if(lis[i] == max_lis and len(lis_items) == 0):
                lis_items.insert(0, num_list[i])
            elif(len(lis_items) > 0 and lis[i] == (last_max_lis -1)):
                lis_items.insert(0, num_list[i])
                last_max_lis = lis[i]

            i = i -1

        return lis_items


def main():
    lis_obj = LIS()
    a1 = [30, 10, 2, 1, 20]
    a2 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    lis = lis_obj.lis(a1)
    print("lis of {0} is\n{1}:{2}\n".format(a1, lis, len((lis))))

if __name__ == '__main__':
    main()