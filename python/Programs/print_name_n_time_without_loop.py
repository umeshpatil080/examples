#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pumesh
#
# Created:     22/01/2018
# Copyright:   (c) pumesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class PrintStr():
    def __init__(self, data):
        self.data = data
        self.count = 0

    def p1(self) : self.count = self.count + 1; print("{0}: {1}\n".format(self.count, self.data))
    def p3(self) : self.p1(); self.p1(); self.p1();
    def p4(self) : self.p3(); self.p1();
    def p20(self): self.p4(); self.p4(); self.p4(); self.p4();
    def p40(self): self.p20(); self.p20();
    def p100(self): self.p40(); self.p40(); self.p20();

def main():
    p = PrintStr('Sam')
    p.p100()


if __name__ == '__main__':
    main()
