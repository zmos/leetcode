s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}"
s_len = len(s)
if s_len < 2:
    print s_len
p = 0
s_l = []
max_len = 0
while p < s_len-1:
    l = []
    q = p + 1
    l.append(s[p])
    while q < s_len:
        if s[q] in l:
            if s[q] in s_l:
                p = p + 1
            else:
                s_l.append(s[q])
                p = s.index(s[q]) + 1
            q = q + 1
            break
        else:
            l.append(s[q])
            q = q + 1
    if len(l) > max_len:
        max_len = len(l)
    if q == s_len:
        print max_len
        break
