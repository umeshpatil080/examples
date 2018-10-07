#-------------------------------------------------------------------------------
# Problem: One away
# There are three type of edits that can be performed on a string: insert a
# character, remove a character, or replace a character. Given two strings
# check if they are one edit(or zero edits) away.
#
# Example:
# pale, ple     => True
# pales, pale   => True
# pale, bale    => True
# pale, bake    => False
#-------------------------------------------------------------------------------

def is_one_away_edit_match(string1, string2):
    # Assume len(string1) > len(string2)
    if not string1 or not string2:
        return False

    str1_len = len(string1)
    str2_len = len(string2)

    if str1_len == 1 and str2_len == 1:
        return True

    len_diff = str1_len-str2_len if str1_len > str2_len else str2_len - str1_len
    if len_diff > 1:
        return False

    mis_match_count = 0
    i = j = 0
    while(i < str1_len and j < str2_len):
        ch1 = string1[i]
        ch2 = string2[j]

        if ch1 != ch2:
            mis_match_count += 1
            if str1_len == str2_len:
                # only replace is possible. After replace characters at 'i'
                # and 'j' are matched. So move to next characters.
                i += 1
                j += 1
            elif str1_len > str2_len:
                # insert in string2 or delete from string1 possible
                if (i+1) < str1_len:
                    if string1[i + 1] == ch2:
                        # delete char at position 'i' in string1
                        i += 1
            elif str2_len > str1_len:
                # insert in string1 or delete from string2 possible
                if (j+1) < str2_len:
                    if string2[j + 1] == ch1:
                        # delete char at position 'j' in string2
                        j += 1
        else:
            i += 1
            j += 1

        if mis_match_count > 1:
            return False

    return True


    return True

def main():
    inputs = [
        {"pale" : "ple"},
        {"pales": "pale"},
        {"pale" : "bale"},
        {"pale" : "bake"},
        {"pale" : "pdle"},
        {"pade" : "ple"},
    ]

    for inp in inputs:
        for string1, string2 in inp.items():
            print("Are '{0}' and '{1}' one way edit: {2}"
            .format(string1, string2, is_one_away_edit_match(string1, string2)))

if __name__ == '__main__':
    main()
