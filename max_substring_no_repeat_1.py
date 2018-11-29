s = "tmmzuxt"
max_len = 0
start = 0
char_index = {}
import pdb; pdb.set_trace()
for index, char in enumerate(s):
    if char in char_index:
        start = char_index[char] + 1
    elif max_len < index - start + 1:
        max_len = index - start + 1
    char_index[char] = index
print max_len
