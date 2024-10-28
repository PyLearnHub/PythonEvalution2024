# 1st


def find_the_weak(properties):
    count = 0
    for i in range(len(properties)):
        j = 1
        if properties[i][0] < properties[j][0] and properties[i][j] < properties[j][j]:
            count += 1
    return count


properties = [[1, 5], [10, 4], [4, 3]]
# properties = [[5, 5], [6, 3], [3, 6]]
# properties = [[2, 2], [3, 3]]
print(find_the_weak(properties))


# 2nd
def fill_the_jug(x, y, t):
    if x + y == t:
        return True


x, y, t = 3, 5, 4
print(fill_the_jug(x, y, t))


# 3rd

def minimum_window(s, t):
    result = ''
    if t[0] not in s:
        return ""
    j = len(t) - 1
    for i in range(len(s)):
        if s[i] == t[0]:
            r = i
            if not i == 0:
                r -= 1
            if t[j] in s[i:]:
                if len(result) < len(s[r + 1:s.index(t[j]) + 1]):
                    result += s[r + 1:s.index(t[j]) + 1]
    return result


s = 'XAYBZC'
t = 'ABC'
# s = "BCAADOBEC"
# s = "ADOBECODEBANC"
# s = "XYZXYZXYZ"
print(minimum_window(s, t))
