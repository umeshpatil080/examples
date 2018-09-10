from time import sleep
from multiprocessing import Process

def _dummy_process(i):
    print("process:" + str(i))
    if i == 5:
        sleep(1)
        raise Exception("Exception in process 0")
    else:
        sleep(5)


def test_logging():
    print("In parent")
    procs = []
    func = _dummy_process
    for i in range(10):
        p = Process(target=func, args = (i,))
        p.start()
        procs.append(p)

    i = 0
    non_zero_exit = 1
    while(non_zero_exit == 1):
        for p in procs:
            non_zero_exit = p.exitcode
            print("exit code of process {0} is: {1}\n".format(i, non_zero_exit))
            if non_zero_exit != 0:
                break
            i = i + 1
        sleep(1)

    if non_zero_exit != 0:
        print("Process {0} encountered some error. So teminating all other processses.".format(i))
        for p in procs:
            p.terminate()
    else:
        print("All processses completed without any error")
    for p in procs:
            p.join()

def main():
    test_logging()

if __name__ == '__main__':
    main()
