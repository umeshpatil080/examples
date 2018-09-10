"""
The dup() system call creates a copy of a file descriptor.

    1. It uses the lowest-numbered unused descriptor for the new descriptor.
    2. If the copy is successfully created, then the original and copy file descriptors may be used interchangeably.
    3. They both refer to the same open file description and thus share file offset and file status flags.

"""

import os


def demo_dup():
    # NOTE: File should exist

    filename = "dup_ex.log"
    with open(filename, 'r+') as file_obj:
        # Create duplicate of file descriptor number associated with
        # file object which points to same underlying file
        dup_fd_no = os.dup(file_obj.fileno())

        # Open duplicate file descriptor to get file object
        # pointing to same same file
        file_obj_dup = os.fdopen(dup_fd_no, 'r+')

        # Write data file using original and duplicated file objects.
        # Data gets written to same file
        file_obj.write("data1")
        file_obj_dup.write("data2")

        # Read data from the file using one of the file object
        fd_dup_read = file_obj_dup.read()

        # Move seek pointer back to the start of the file
        os.lseek(file_obj_dup.fileno(), 0, 0)

        # Read file using other file object
        fd_read = file_obj.readline()


        print("fd_read:{0}\nfd_dup_read:{1}\n".format(fd_read, fd_dup_read))

        file_obj_dup.close()


def main():
    demo_dup()

if __name__ == '__main__':
    main()
