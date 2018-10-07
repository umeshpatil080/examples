#-------------------------------------------------------------------------------
# Problem: Given two strings, determine if one string is permutaion of another
#-------------------------------------------------------------------------------

def is_permuted_strings(string1, string2):
    if not string1 or not string2:
        return False

    if len(string1) != len(string2):
        return False

    str_len = len(string1)
    str1_char_count = {}
    str2_char_count = {}
    i = 0
    while i < str_len:
        ch1 = string1[i]
        ch2 = string2[i]

        char_count = str1_char_count[ch1] if ch1 in str1_char_count else 0
        str1_char_count[ch1] = char_count + 1

        char_count = str2_char_count[ch2] if ch2 in str2_char_count else 0
        str2_char_count[ch2] = char_count + 1

        i += 1

    if len(str1_char_count) != len(str2_char_count):
        return False

    for ch, count in str1_char_count.items():
        if ch in str2_char_count:
            if count != str2_char_count[ch]:
                return False
        else:
            return False

    return True

def main():
    string1 = "abcb"
    string2 = "abbc"
    print("Are '{0}' and '{1}' permutations of each other: {2}"
    .format(string1, string2, is_permuted_strings(string1, string2)))

if __name__ == '__main__':
    main()
