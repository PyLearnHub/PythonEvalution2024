#Problem 1 : Find the count of Weak characters.
#Pseudo-Code:
"""
Function weakCount(characters):
    char_length = length of characters
    count = Initially zero

    for i from char_length:
        is_weak = false            #setting a flag for each iteration
        for j from char_length:
            if i not equals j:     #ensuring we don't compare same lists
                if character[i][0] less than character[j][0] and character[i][1] less than character[j][1]:
                #Condition 1: Checking for the first characters attack with next characters attack
                #Condition 2: Checking for the first characters defence with next characters defence
                    is_weak = True
        if is_weak is True:
            Increment count by 1
    return count
"""
#Solution:


def weak_count(characters):
    char_length = len(characters)
    count = 0

    for i in range(0, char_length):
        is_weak = False
        for j in range(0, char_length):
            if i != j:
                if (characters[i][0] < characters[j][0]) and (characters[i][1] < characters[j][1]):
                    is_weak = True
                    break
        if is_weak:
            count += 1
    return count


test_case1 = [[5, 5], [6, 3], [3, 6]]
test_case2 = [[2, 2], [3, 3]]
test_case3 = [[1, 5], [10, 4], [4, 3]]
test_case4 = [[1, 5], [5, 1], [10, 4], [4, 3]]
print(weak_count(test_case1))
print(weak_count(test_case2))
print(weak_count(test_case3))
print(weak_count(test_case4))
