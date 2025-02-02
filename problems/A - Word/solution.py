def program(s):
    lower = 0
    upper = 0
    for i in range(len(s)):
        code = ord(s[i])
        if 97 <= code <= 122:
            lower += 1
        else:
            upper += 1
    if lower < upper:
        return s.upper()
    else:
        return s.lower()
 
s = input().strip()
 
print(program(s))