import math


def find_weak_characters(characters):
    """
        Count the number of weak characters in a game based on their attack and defense properties.

        A character is considered weak if there exists another character with strictly greater attack
        and defense levels.

        Parameters:
        characters (List[List[int]]): A list of characters where each character is represented
                                       as a list containing [attack, defense].

        Returns:
        int: The number of weak characters.
    """
    weak_characters = 0
    for i in range(len(characters) - 1):
        for j in range(i + 1, len(characters)):
            if (characters[i][0] < characters[j][0] and characters[i][1] < characters[j][1]
                    or characters[i][0] > characters[j][0] and characters[i][1] > characters[j][1]):
                weak_characters += 1
    return weak_characters


def find_minimum_window(source_str, target):
    """
        Find the minimum window in 'source_str' that contains all characters from 'target'.

        This function checks all possible substrings of 'source_str' to find the smallest substring
        that contains all characters from 'target'.

        Parameters:
        source_str (str): The string in which to search for the minimum window.
        target (str): The string containing the characters that must be included in the window.

        Returns:
        str: The minimum window substring if found; otherwise, an empty string.
    """
    for window_size in range(len(target), len(source_str) + 1):
        for start_index in range(len(source_str) + 1):
            if start_index + window_size <= len(source_str):
                current_window = source_str[start_index:start_index + window_size]
                matching_chars = len(target)
                for char in target:
                    if char in current_window:
                        matching_chars -= 1
                if matching_chars == 0:
                    return source_str[start_index:start_index + window_size]
    return ''


def fill_jugs_to_target(jug1, jug2, target_litres):
    """
        Determine if it is possible to measure exactly 'target_litres' using two jugs.

        The function checks whether 'target_litres' can be measured using two jugs with capacities
        'jug1' and 'jug2'. It uses properties of GCD to determine feasibility.

        Parameters:
        jug1 (int): The capacity of the first jug.
        jug2 (int): The capacity of the second jug.
        target_litres (int): The desired amount of water to measure.

        Returns:
        bool: True if it is possible to measure 'target_litres', otherwise False.
    """
    if target_litres > jug1 + jug2:
        return False
    return target_litres % math.gcd(jug1, jug2) == 0


def formula_aligner(formula):
    """
        Parse a chemical formula and return the count of each atom in sorted order.

        This function processes a string representing a chemical formula, handling
        nested structures defined by parentheses. It counts the occurrences of each
        atom and returns a formatted string where each atom is followed by its count
        (if greater than 1), sorted alphabetically.

        Parameters:
        formula (str): A string representing the chemical formula to be parsed.
                       The formula may contain atoms represented by uppercase
                       letters followed by optional lowercase letters, digits
                       indicating counts, and nested groups enclosed in parentheses.

        Returns:
        str: A string representation of the counts of each atom in sorted order.
             For example, "H2O" for two hydrogen atoms and one oxygen atom.

        Example:
            Input: "Mg(OH)2"
            Output: "H2MgO2"
    """
    atom_count = {}
    atom_holder = []
    index = 0

    while index < len(formula):
        if formula[index] == '(':
            atom_holder.append(atom_count.copy())
            atom_count = {}
            index += 1
        elif formula[index] == ')':
            index += 1
            multiplier = 0
            while index < len(formula) and formula[index].isdigit():
                multiplier = multiplier * 10 + int(formula[index])
                index += 1
            multiplier = multiplier if multiplier > 0 else 1
            for atom, count in atom_count.items():
                if atom in atom_holder[-1]:
                    atom_holder[-1][atom] += count * multiplier
                else:
                    atom_holder[-1][atom] = count * multiplier
            atom_count = atom_holder.pop()
        else:
            j = index + 1
            while j < len(formula) and formula[j].islower():
                j += 1
            atom = formula[index:j]
            index = j
            count = 0
            while index < len(formula) and formula[index].isdigit():
                count = count * 10 + int(formula[index])
                index += 1
            if count == 0:
                count = 1
            if atom in atom_count:
                atom_count[atom] += count
            else:
                atom_count[atom] = count
    result = []
    for atom in sorted(atom_count.keys()):
        result.append(atom)
        if atom_count[atom] > 1:
            result.append(str(atom_count[atom]))
    return ''.join(result)


# properties = [[5, 5], [6, 3], [3, 6]]
# properties = [[2, 2], [3, 3]]
properties = [[1, 5], [10, 4], [4, 3]]
print(find_weak_characters(properties))

# source_str = "BCAADOBEC"
# source_str = 'AXYD'
source_str = "ABWFCDEBCDA"
target = "ABC"
print('Minimum window :', find_minimum_window(source_str, target))

print(fill_jugs_to_target(3, 5, 4))
print(fill_jugs_to_target(2, 6, 5))
print(fill_jugs_to_target(1, 2, 3))

# print(formula_aligner("H2O"))  # Output: "H2O"
# print(formula_aligner("Mg(OH)2"))  # Output: "H2MgO2"
print(formula_aligner("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"
