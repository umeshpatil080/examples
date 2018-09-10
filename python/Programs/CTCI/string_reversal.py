#-------------------------------------------------------------------------------
# Reversing a string
#-------------------------------------------------------------------------------

class StrReversal():
    def __init__(self):
            pass

    def reverse(self, string = ""):
        if(not string):
            return string

        lstring = list(string)
        n = len(lstring)
        i = 0
        while(i < n/2):
            tmp = lstring[i]
            lstring[i] = lstring[n-1-i]
            lstring[n-1-i] = tmp
            i += 1
        rstring = "".join(lstring)
        return rstring

def main():
    strRev = StrReversal()
    string = "ABCD"
    rstring = strRev.reverse(string)
    print("string  :{0}\nrstring: {1}".format(string, rstring))

if __name__ == '__main__':
    main()
