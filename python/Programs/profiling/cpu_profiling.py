import re
from memory_profiler import profile

sample_data_file = "sample_data.txt"

def read_data(file_path:str):
    words = []
    count = 0
    with open(file_path, "r",  encoding='utf-8') as file1:
        while True:
            count += 1
  
            # Get next line from file 
            line = file1.readline() 
        
            # if line is empty 
            # end of file is reached 
            if not line: 
                break
            if line not in ['\n', '\r\n']:
                words.append(line.split())
    return words

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    my_func1()
    del b
    return a

class Sam():
    def __init__(self):
        pass

    def test(self):
        print("In Sam.test")

def sam(obj:Sam):
    obj.test()

def main():
    #words = read_data(sample_data_file)
    #my_func()
    obj = Sam()
    sam(obj)

if __name__ == "__main__":
    main()