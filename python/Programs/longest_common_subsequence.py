"""
Examples:
LCS for input Sequences 'ABCDGH' and 'AEDFHR' is 'ADH' of length 3.
LCS for input Sequences 'AGGTAB' and 'GXTXAYB' is 'GTAB' of length 4.

"""

import sys

class LCS():
    def __init__(self):
        pass

    def get_lcs(self, seq1, seq2):
        if(len(seq1) == 0 or len(seq2) == 0):
            return None

        m = len(seq1) + 1
        n = len(seq2) + 1
        dp_lcs_matrix = [[0 for x in range(n)] for y in range(m)]
        self._print_matrix(dp_lcs_matrix)

        i = 0
        j = 0
        while(i < m -1):
            j = 0
            r = i + 1
            while(j < n -1):
                c = j + 1
                print("i:{0}\tj:{1}".format(i, j))
                print("r:{0}\tc:{1}\n".format(r, c))
                if(seq1[i] == seq2[j]):
                    dp_lcs_matrix[r][c] = dp_lcs_matrix[r-1][c-1] + 1
                else:
                    dp_lcs_matrix[r][c] =max(dp_lcs_matrix[r-1][c], dp_lcs_matrix[r][c-1])
                j = j + 1
            i = i + 1

        print("\nDP LCS matrix:\n")
        self._print_matrix(dp_lcs_matrix)

        # TODO: Find lcs substring characters correctly
        i = m - 1
        j = n - 1
        lcs = []
        while(i > 0 and j > 0):
            if(dp_lcs_matrix[i][j] == (dp_lcs_matrix[i-1][j-1] + 1)):
                lcs.insert(0, seq2[j-1])
                i = i -1
                j = j -1
            elif(dp_lcs_matrix[i-1][j] > dp_lcs_matrix[i][j-1]):
                # moving up the row
                # lcs[i][j] = came from above row element is the same column cell
                i = i - 1
            else:
                # moving to a column left
                # lcs[i][j] = came from element in the same which is left of current cell
                j = j - 1


        print("LCS:{0}".format(lcs))
        return dp_lcs_matrix[m-1][n-1]


    def _print_matrix(self, two_dim_matrix):
        for r in two_dim_matrix:
            for c in r:
                data = "{0}\t".format(c)
                sys.stdout.write(data)
            print("")

def main():
    lcs_obj = LCS()
    seq1 = "ABCDGH"
    seq2 = "AEDFHR"

    seq3 = "AGGTAB"
    seq4 = "GXTXAYB"
    lcs = lcs_obj.get_lcs(seq1, seq2)

    print("LCS of '{0}' and '{1}' is: '{2}'".format(seq1, seq2, lcs))

if __name__ == '__main__':
    main()
