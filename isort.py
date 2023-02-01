def isort(s):
    if len(s) <= 1:
        return s
    for i in range(1,len(s)):
        x = s[i]
        j = i-1
        while j >= 0 and x < s[j]:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = x
    return s
