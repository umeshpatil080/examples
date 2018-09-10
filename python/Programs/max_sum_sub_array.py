"""
Largest Sum Contiguous Subarray: https://en.wikipedia.org/wiki/Maximum_subarray_problem
(Kadane's algorithm)

"""


class MaxSubSubSequence():
    def __init__(self):
        pass

    def get_max_sum_subsequence(self, seq):
        if(not seq):
            return 0

        max_ending_here = max_so_far = 0
        for x in seq:
            max_ending_here = max(x, max_ending_here + x)   # what is max sum considering value x at ith position
            max_so_far = max(max_ending_here, max_so_far)   # what is max value so far

        return max_so_far

    def get_seq_max_subsequence(self, seq):
        if(not seq):
            return None
        else:
            m = n = -1
            max_ending_here = max_so_far = 0
            prev_max_ending = 0
            i = 0
            while(i < len(seq)):
                x = seq[i]

                if((max_ending_here + x) > x):
                    max_ending_here = max_ending_here + x
                else:
                    max_ending_here = x

                if(max_ending_here > max_so_far):
                    max_so_far = max_ending_here
                    n = i

                i = i + 1

                # n gives the index of last item in the sub sequence with max sum
                # Traverse back from n to match max sum to deteremine start of the sequence

            i = n
            sum_so_far = 0
            while(i >= 0):
                x =  seq[i]
                sum_so_far = sum_so_far + x
                if(sum_so_far == max_so_far):
                      m = i
                      break
                i = i -1

            print("Max sum = {0}\nStart Index = {1}\nEnd Index = {2}\n".format(max_so_far, m, n))




def main():
    seq = [-2, -3, 4, -1, -2, 1, 5, -3, 10]
    seq1 = [-2, -3, 4, -1, -2, 1, 5, -8, 10]
    obj = MaxSubSubSequence()
    res = obj.get_max_sum_subsequence(seq)
    #print("Result:{0}\n".format(res))

    obj.get_seq_max_subsequence(seq)

if __name__ == '__main__':
    main()
