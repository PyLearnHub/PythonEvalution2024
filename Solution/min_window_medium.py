#Problem-3: Minimum window function
#Pseudo-Code:
"""
Function minimum_window(s, t):
    if s and t are empty:
        return ""       empty string since either s or t is empty
    least_window = ""   initially empty string
    for p1 in range of length of s:
        for p2 in range between p1 and length of s:
            substring = s[p1 to p2 + 1]  
            if contains_character(substring, t):     Custom function to check the each characters return True or False
                if least_window equals '' or length of substring is smaller than length of least_window:
                    least_window = substring   
                    #Checks if the least is empty or compares if substring length is smaller than least window
    return least_window
    
Function contains_character(substring, t):
    for letter in t:
        if letter not in substring:
            return False
        return True
"""


def minimum_window(s, t):
    if not s or not t:
        return ''

    least_window = ''

    for p1 in range(len(s)):
        for p2 in range(p1, len(s)):
            substring = s[p1:p2+1]
            if contains_character(substring, t):
                if least_window == "" or len(substring) < len(least_window):
                    least_window = substring
    return least_window


def contains_character(substring, t):
    for letter in t:
        if letter not in substring:
            return False
    return True

# Testcases:
#Input: s = "ADOBECODEBANC", t = "ABC"
#Expected Output: "BANC"

# Input: s = "XAYBZC", t = "ABC"
# Expected Output:: "AYBZC"

# Input: s = "BCAADOBEC", t = "ABC"
# Expected Output: "BCA"

print(minimum_window("ADOBECODEBANC", "ABC"))
print(minimum_window("XAYBZC", "ABC"))
print(minimum_window("BCAADOBEC", "ABC"))
print(minimum_window("XYZXYZXYZ", "ABC"))
 
