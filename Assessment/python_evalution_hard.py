
def formula_aligner(formula):
    len_of_formula = len(formula)
    formula_dict = {}
    for i in range(len_of_formula):
        if not (formula[i].islower() or formula[i] == ')' or formula[i] == '('):
            if formula[i] not in formula_dict.keys():
                if formula[i].isupper() and i < len_of_formula-1 and formula[i + 1].islower():
                    if formula[i + 2].isnumeric():
                        formula_dict[formula[i] + formula[i + 1]] = formula[i + 2]
                    else:
                        formula_dict[formula[i] + formula[i + 1]] = 1
                elif formula[i].isupper() and i < len_of_formula-1 and formula[i + 1].isnumeric():
                    formula_dict[formula[i]] = formula[i + 1]
                elif not formula[i].isnumeric():
                    formula_dict[formula[i]] = 1
    return formula_dict


# f = "H2O"
# f = "Mg(OH)2"
f = "K4(ON(SO3)2)2"
# print(formula_aligner(f))
