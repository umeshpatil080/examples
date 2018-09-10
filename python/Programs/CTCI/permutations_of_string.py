#-------------------------------------------------
# Problem: Finding permutaions of given string
#-------------------------------------------------

j = 1
def permutation(prefix = "", string = ""):
    n = len(string)
    global j
    if(n == 0):
        print(str(j) + ":" + prefix)
        j += 1

    i = 0
    while(i < n):
        ith_char = string[i]
        permutation(prefix + ith_char, string[0:i] + string[i+1:])
        i += 1

def main():
    string = "ABC"
    permutation("", string)

if __name__ == '__main__':
    main()
