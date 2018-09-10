import os
import sys

class RedirectStdStreams():
    def __init__(self, stdout = None, stderr = None) :
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.stdout_org = sys.stdout
        self.stderr_org = sys.stderr

        sys.stdout.flush()
        sys.stderr.flush()

        sys.stdout = self._stdout
        sys.stderr = self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.stdout_org
        sys.stderr = self.stderr_org

        # This is important. Return True indicates
        # that we are taking care of any error and
        # clean up is being done here
        return True



def main():
    print("Before redirection")
    with open('redirected.log', 'w') as fd:
        with RedirectStdStreams(stdout = fd, stderr = os.devnull):
            print("Inside redirection")

    print("Outside redirection")

if __name__ == '__main__':
    main()
