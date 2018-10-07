#-------------------------------------------------------------------------------
# Problem: Palindrome Permutation
# Given a string, check if it is permutation of a palindrome string.
# Check if a palindrome can be constructed from the characters in a string
#-------------------------------------------------------------------------------

def is_permuted_palindrome(string):
    str_len = len(string)

    if str_len == 1:
        return True

    char_count = {}
    space_count = 0
    for ch in string:
        if ch != ' ':
            char_count[ch] = (char_count[ch] + 1) if ch in char_count else 1
        else:
            space_count += 1

    odd_num_chars = 0
    for ch, value in char_count.items():
        if value % 2 != 0:
            odd_num_chars += 1

    if odd_num_chars == 0:
        return True
    elif odd_num_chars == 1 and (str_len - space_count) % 2 !=0:
        return True
    else:
        return False

def main():
    string = "tact coa"
    print("Is '{0}' a permuted palindrome: {1}".format(string, is_permuted_palindrome(string)))

if __name__ == '__main__':
    main()
