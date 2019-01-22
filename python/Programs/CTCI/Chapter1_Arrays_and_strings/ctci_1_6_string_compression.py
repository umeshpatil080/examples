#-------------------------------------------------------------------------------
# String compression:
# Implement basic string compression mechanism based on the
# count of repeated characters. If compressed string is shorter than original
# string then, return original string.
#
# Example: aabcccccaaa => a2b1c5a3
#-------------------------------------------------------------------------------

class CompressRepeatedChars():
    def __init__(self):
        pass

    @classmethod
    def compress(cls, string):
        compressed_str = ""
        str_len = len(string)
        i = 0
        repeat_char_count = 0
        prev_char = None
        while(i < str_len):
            cur_char = string[i]
            if prev_char:
                if prev_char == cur_char:
                    repeat_char_count += 1
                else:
                    compressed_str += prev_char + str(repeat_char_count)
                    repeat_char_count = 1
            else:
                repeat_char_count = 1

            prev_char = cur_char
            i += 1

        compressed_str += prev_char + str(repeat_char_count)
        return compressed_str if len(string) >= len(compressed_str) else compressed_str

    @classmethod
    def compress_method1(cls, string):
        compressed_str = ""
        str_len = len(string)
        i = 0
        repeat_char_count = 0
        while(i < str_len):
            cur_char = string[i]
            j = i
            while(j < str_len):
                 if cur_char == string[j]:
                    j += 1
                 else:
                    break
            repeat_char_count = j - i + 1 # default len 1 for single character
            i = j
            compressed_str += compressed_str + cur_char + str(repeat_char_count)
        return compressed_str if len(compressed_str) < len(string) else string



def main():
    #string = "aabcccccaaa"
    inputs = ["aabcccccaaa", "a"]
    for string in inputs:
        compressed_str = CompressRepeatedChars.compress(string)
        compressed_str1 = CompressRepeatedChars.compress_method1(string)
        print("Original string: {0}\nCompressed string: {1}\nCompressed string: {1}"
        .format(string, compressed_str, compressed_str1))

if __name__ == '__main__':
    main()
