"""
The dup2() system call is similar to dup() but the basic difference
between them is that instead of using the lowest-numbered unused file
descriptor, it uses the descriptor number specified by the user.

# 0 -> stdin, 1-> stdout, 2 -> stderr

"""

import os
import sys


def _filedes(f_or_fd):
    fdec = getattr(f_or_fd, 'fileno', lambda: f_or_fd)()
    if not isinstance(fdec, int):
        raise ValueError("File_name.fileno() or a int descriptor Expected")
    return fdec

def demo_dup2():

    # Open a file
    fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

    # Write one string
    os.write(fd, b'This is test')

    # Now duplicate this file descriptor as 1000
    fd2 = 1000
    os.dup2(fd, fd2);

    # Now read this file from the beginning using fd2.
    os.lseek(fd2, 0, 0)
    str = os.read(fd2, 100)
    print("Read String is : ", str)

    # Close opened file
    os.close( fd )

    print("Closed the file successfully!!")

def main():
    demo_dup2()

if __name__ == '__main__':
    main()
