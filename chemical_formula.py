def sort_the_formula(formula):
        s = ""
        chemical_list = list(formula)
        sort_list = sorted(chemical_list)
        for char in sort_list:
                if char.isupper():
                        s += char
                        index = chemical_list.index(char)
                        if index != len(chemical_list) - 1:
                                if chemical_list[index + 1].isdigit() or chemical_list[index + 1].islower():
                                        s += chemical_list[index + 1]
        return s


def chemical_formula(formula):
        if '(' not in formula:
                return sort_the_formula(formula)
        else:
                st = formula[:formula.index('(')]
                st2 = formula[formula.index('(') + 1: formula.index(')')]
                st3 = ""
                for ele in st2:
                        ele += formula[formula.index(')') + 1]
                        st3 += ele
                return sort_the_formula(st + st3)


result = chemical_formula("H2O")
print(result)
