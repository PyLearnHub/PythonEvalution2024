#Problem 2: Return whether the total amount of water in both jugs may reach target
#Conditions:
# Either Jug must be fully filled
# Or jug can be fully emptied
# Or Transferring can be done till filled.
#Pseudo-Code:
"""
x - Jug x with capacity in litres
y - Jug y with capacity in litres
target - Target to achieve 

Function reach_target(x, y, target):
    if target is greater than sum of x, y:
        return false
    else if target equals x and y or target equals x or target equals y:
        return True
    else if reminder of target and GCD of x,y != 0:
        return False
    else:
        return False

Test Cases:
Testcases:
Example 1:
Input: x = 3, y = 5, target = 4 Output: true
Explanation:
Follow these steps to reach a total of 4 liters:
Fill x = 0, y = 5         --> (0, 5).
Y(5 - 3 = 2) X(0 + 3 = 3) --> (3, 2).
Empty X                   --> (0, 2).
Y To X                    --> (2, 0).
Fill X                    --> (2, 5).
Y to X                    --> (3, 4).
Empty X                   --> (0, 4).
OutPut = True

Example 2:
Input: x = 2, y = 6, target = 5 
Output: false

Example 3:
Input: x = 1, y = 2, target = 3 
Output: true
"""
import math



def reach_target(x, y, target):
    if target > x + y:
        return False
    elif target % math.gcd(x, y) != 0:
        return False
    elif (target == x + y) or (target == x) or (target == y):
        return True
    return True


x = int(input("Enter the capacity of the Jug X :"))
y = int(input("Enter the capacity of the Jug Y :"))
target = int(input("Enter the target to achieve :"))
print(reach_target(x, y, target)) 
