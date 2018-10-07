#-------------------------------------------------------------------------------
# CTCI 1.1: Determine if a string has all the unique characters.
#           What if you cannot use any additional data structures?
#-------------------------------------------------------------------------------

# Method 1: Using a dictionary

# Assuming string has ASCII set(0-127)
# Time complexity : O(n)
# Space complexity:
def is_unique_char_string(string):
    track_char = {}
    for ch in string:
        if ch in track_char:
            return False
        else:
            track_char[ch] = True
    return True

# Other non-optimal solutions
# 1. Sort the string and if there are any consecutive duplicate charcters
# 2. Compare each character with every other character in the string

#2
# Time complexity: n + (n-1) + (n-2) + ...+ 1
def is_unique_char_string_by_char_comp(string):
    str_len = len(string)
    i = j = 0
    while i < str_len:
        j = i + 1
        while j < str_len:
            if string[i] == string[j]:
                return False
            j += 1
        i += 1
    return True

def main():
    string = '12abcd'
    print("Does '{0}' has unique characters: {1}".format(string, is_unique_char_string(string)))
    print("Does '{0}' has unique characters: {1}".format(string, is_unique_char_string_by_char_comp(string)))

if __name__ == '__main__':
    main()
