import sys


def count_weak_characters(characters): # problem 3
    """Used to return the number of week characters from the given characters"""
    total_weak_characters = 0
    attack = 0
    defence = 1
    for character in range(0, len(characters) - 1):
        for step in range(character + 1, len(characters)):
            if characters[character][attack] < characters[step][attack] and characters[character][defence] < \
                    characters[step][defence]:
                total_weak_characters += 1
                break
            elif characters[step][attack] < characters[character][attack] and characters[step][defence] < \
                    characters[character][defence]:
                total_weak_characters += 1
                break

    return total_weak_characters


def is_jug_fill(jug_1, jug_2, target): # problem 2
    """
    Determines if both jugs can achieve the target
    """
    if jug_1 == target or jug_2 == target or (jug_1 + jug_2 == target):
        return True
    elif jug_2 + jug_1 > target:
        return False
     elif target == math.gcd(jug_1, jug_2) == 0:
        return True
    else:
        return False


def fin_min_window(s, t): # problem 1
    """Used to find the minimum window as a substring in s with respect to t"""
    visited_marking = {}
    min_window_size = sys.maxsize
    print(len(s))
    print(len(t))
    answer = ""
    for character in t:
        visited_marking[character] = False

    for start in range(0, (len(s) - len(t) + 1)):
        end = start
        set_flag_count = 0
        while end < len(s) and (not (set_flag_count == len(t))):
            if s[end] in t and (not (visited_marking[s[end]])):
                visited_marking[s[end]] = True
                set_flag_count += 1
            end += 1
        temp = s[start:end]
        if min_window_size > len(temp) and not (False in visited_marking.values()):
            answer = temp
            min_window_size = len(answer)
        if not (False in visited_marking.values()):
            for character in t:
                visited_marking[character] = False
    return answer


characters = [[5, 5], [6, 3], [3, 6]]
print(count_weak_characters(characters))

s = "XYZXYZXYZ"
t = "ABC"
print("answer", fin_min_window(s, t))
