import sys

def redirect_to_file(text):
    original = sys.stdout
    sys.stdout = open('redirect.txt', 'w')
    print('This is your redirected text:')
    print(text)
    sys.stdout = original

    print('This string goes to stdout, NOT the file!')

if __name__ == '__main__':
    # Redirecting stdout / stderr
    redirect_to_file('Python rocks!')