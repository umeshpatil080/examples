#-------------------------------------------------------------------------------
# Problem statement: Write a metod to rotate a m*n metrix by 90 degress.
#-------------------------------------------------------------------------------

import sys

def read_matrix(m = 4, n = 4):
    matrix = [[0 for j in range(n)] for i in range(m)]

    """
    # Reading matrix from user console
    for i in range(m):
        line = input()
        ith_row_items = line.split()
        if len(ith_row_items) == n:
            for j in range(n):
                matrix[i][j] = ith_row_items[j]
        else:
            raise "Not sufficient items enetered for the row " + str(i)

    print("matrix:")
    print(matrix)
    """
    return matrix

def print_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            sys.stdout.write(str(matrix[i][j]) + "\t")
        print("\n")

def main():
    matrix = read_matrix(2, 4)
    print_matrix(matrix)

if __name__ == '__main__':
    main()
