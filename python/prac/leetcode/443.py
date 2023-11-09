# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

class Solution:
    def compress(self, chars: List[str]) -> int:
        def get_nums(diff):
            lst = []
            while diff > 0:
                lst.append(str(diff%10))
                diff = diff//10
            return lst[::-1]
    
        ptr,start,end,counter = 0,0,0,0
        while end <= len(chars):
            end_loop = end == len(chars)
            if (end_loop or (chars[start] != chars[end])):
                chars[ptr] = chars[start]
                ptr += 1
                counter = end - start
                start = end
                if counter > 1:
                    temp_lst = get_nums(counter)
                    chars[ptr:ptr + len(temp_lst)] = temp_lst
                    ptr += len(temp_lst)
                if end_loop:
                    break
            else:
                end += 1
        return ptr