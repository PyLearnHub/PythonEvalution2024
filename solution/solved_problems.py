from collections import defaultdict
import math


def find_weak_characters(properties):
    """
    Counts the number of weak characters in a game based on their attack and defense properties.

    A character is considered weak if there exists another character with both
    higher attack and defense values.

    Parameters:
    properties (List[List[int]]): A 2D list where each sublist contains two integers
                                   representing the attack and defense of a character.

    Returns:
    int: The count of weak characters in the provided list of properties.
    """
    n = len(properties)

    i = 0
    weak_count = 0
    while i < n:
        attack = properties[i][0]
        defense = properties[i][1]
        for j in range(n):
            if j != i:
                if attack < properties[j][0] and defense < properties[j][1]:
                    weak_count += 1
                    break
        i += 1
    return weak_count


def is_jugs_filled_target(jug1, jug2, target):
    """
    Determines if it is possible to measure exactly the target amount of water
    using two jugs with given capacities.

    The function uses the properties of the greatest common divisor (GCD)
    to check whether the target amount can be measured using the jugs.

    Parameters:
    x (int): The capacity of the first jug.
    y (int): The capacity of the second jug.
    target (int): The desired amount of water to measure.

    Returns:
    bool: True if the target amount can be measured using the two jugs,
          False otherwise.
    """
    if jug1 + jug2 < target:
        return False

    gcd = math.gcd(jug1, jug2)
    if target % gcd == 0:
        return True
    return False


def minimum_window(s, t):
    """
    Finds the minimum window substring of `s` that contains all the characters
    of the string `t`.

    The function examines all possible substrings of `s` and checks if they
    contain all characters from `t`. It keeps track of the shortest valid
    substring found during the process.

    Parameters:
    s (str): The input string in which to search for the minimum window.
    t (str): The string containing the characters that must be included in the window.

    Returns:
    str: The minimum window substring that contains all characters of `t`.
         If no such window exists, returns an empty string.
    """
    min_window = ""
    min_length = float('inf')
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            window = s[i:j]

            count = 0
            for k in range(len(t)):
                if t[k] in window:
                    count += 1
            if count == len(t):
                if min_length > len(window):
                    min_length = len(window)
                    min_window = window
    return min_window


def count_of_atoms(formula):
    """
    Parses a chemical formula and counts the occurrences of each atom.

    The function processes the input `formula`, which can include atomic elements
    with optional counts, as well as nested groupings denoted by parentheses. It
    returns a string representing the count of each atom in sorted order.

    Parameters:
    formula (str): A string representing the chemical formula to parse.
                   It may contain uppercase and lowercase letters, digits,
                   and parentheses.

    Returns:
    str: A string representing the sorted count of each atom in the format
         "ElementCount", where `Count` is included only if greater than 1.
         For example, "H2O" for water, "K4N2O14S4" for a complex formula.
    """
    prev_count_stack = []
    current_count = defaultdict(int)
    i = 0

    while i < len(formula):
        if formula[i].isupper():
            j = i + 1
            while j < len(formula) and formula[j].islower():
                j += 1
            element = formula[i:j]
            i = j

            count = 0
            while i < len(formula) and formula[i].isdigit():
                count = count * 10 + int(formula[i])
                i += 1
            current_count[element] += count if count > 0 else 1

        elif formula[i] == '(':
            prev_count_stack.append(current_count)
            current_count = defaultdict(int)
            i += 1

        elif formula[i] == ')':
            i += 1
            count = 0

            while i < len(formula) and formula[i].isdigit():
                count = count * 10 + int(formula[i])
                i += 1

            count = count if count > 0 else 1

            for element in current_count:
                current_count[element] *= count

            if prev_count_stack:
                previous_count = prev_count_stack.pop()
                for element, cnt in current_count.items():
                    previous_count[element] += cnt
                current_count = previous_count

    result = []
    for element in sorted(current_count.keys()):
        if current_count[element] > 1:
            result.append(f"{element}{current_count[element]}")
        else:
            result.append(f"{element}")

    return ''.join(result)


weak_characters = find_weak_characters([[1, 5], [10, 4], [4, 3]])
print(weak_characters)

is_filled = is_jugs_filled_target(3, 5, 4)
print(is_filled)

shortest_window = minimum_window("ADOBECODEBANC", "ABC")
print(shortest_window)

count_of_elements = count_of_atoms("K4(ON(SO3)2)2")
print(count_of_elements)

