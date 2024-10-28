def find_number_of_atoms(formula, multiply, answer):
    """used to find the number of atoms in a formula for each element"""
    # base condition
    start = 0
    element = ""
    while start < len(formula):

        if formula[start].isupper():
            element += formula[start]
            start += 1
        elif formula[start].islower():
            element += formula[start]
            start += 1
        elif ord(formula[start]) == 40:
            pass # Recursion call happens here
        elif 2 <= int(formula[start]) <= 9:  # if the following character is number
            temp = start + 1
            times = 1
            number = 0
            try:
                while 2 <= int(formula[temp]) <= 9:
                    # add the preceding numbers to the number so that double digits can be handled
                    number += int(formula[temp]) * times
                    times *= 10
            except ValueError as e:
                find_number_of_atoms(formula[start+1:], multiply, answer)
