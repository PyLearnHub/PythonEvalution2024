def minimum_window(s, t):
    res = ""
    sum1 = float('inf')
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            s2 = s[i:j]

            count = 0
            for k in range(len(t)):
                if t[k] in s2:
                    count += 1
            if count == len(t):
                if sum1 > len(s2):
                    sum1 = len(s2)
                    res = s2
    return res


result = minimum_window("ADOBECODEBANC", "ABC")
print(result)
