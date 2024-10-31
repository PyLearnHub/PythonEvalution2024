#Problem 4: Expanding Chemical Formula
#Pseudo-Code:
"""
Function expand_formula(formula):
    element_count = {}  initializing empty dict to store the count of each element
    i = 0    for traversing
    while i less than length of formula:
        if formula[i] contains '(':     Nested elements are checked
            initialize start equals i
            i += 1 
            while i less than length of formula and formula[i] does not contain ')':
                i += 1
            i += 1
            
            multiplier = 0       to find the number
            while i less than length of formula and formula[i] is digit:
                multiplier = multiplier * 10 + int(formula[i])
                i += 1
            if multiplier is zero:
                multiplier equals 1
            
            for j starting from start+1 and i subtracted to the length of multiplier - 1:
                if formula is alphanumeric:
                    element = formula[j]
                    while j + 1 less than length of formula and formula of j+1 is lower character:
                        j += 1
                    element_count[element] = element_count.get(element, 0) + multiplier
                    
        else:
            start equals i
            i incremented by 1
            while i less than length of formula and formula[i] is lower:
                count = count * 10 + int(formula)
                i incremented by 1
            if count is 0
                increment by 1
            element_count[element] = element_count.get(element, 0) + count
    
    result = ""
    for element in sorted element_count:
        result = result added to element
        if element_count[element] greater than 1: 
            result += str(element_count(element))
    return result
            
"""


def expand_formula(formula):
    element_count = {}
    i = 0

    while i < len(formula):
        if formula[i] == '(':
            start = i
            i += 1
            while i < len(formula) and formula[i] != ')':
                i += 1
            i += 1
            multiplier = 0
            while i < len(formula) and formula[i].isdigit():
                multiplier = multiplier * 10 + int(formula[i])
                i += 1
            if multiplier == 0:
                multiplier = 1
            for j in range(start+1, i - len(str(multiplier)) - 1):
                if formula[j].isalpha():
                    element = formula[j]
                    while j + 1 < len(formula) and formula[j + 1].islower():
                        j += 1
                    element_count[element] = element_count.get(element, 0) + multiplier
        else:
            start = i
            i += 1
            while i < len(formula) and formula[i].islower():
                i += 1
            element = formula[start:i]
            count = 0
            while i < len(formula) and formula[i].isdigit():
                count = count * 10 + int(formula[i])
                i += 1
            if count == 0:
                count = 1
            element_count[element] = element_count.get(element, 0) + count

    result = ""
    for element in sorted(element_count):
        result += element
        if element_count[element] > 1:
            result += str(element_count[element])
    return result


print(expand_formula("H2O"))
print(expand_formula("Mg(OH)2"))
print(expand_formula("K4(ON(SO3)2)2"))
