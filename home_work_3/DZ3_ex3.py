# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(*args):
    names = {}
    for nm in args:
        first_letter = nm[0]
        if first_letter not in names:
            names[first_letter] = [nm]
        else:
            names[first_letter].append(nm)
    return names


print(thesaurus('Harry', 'Ron', 'Hermiona', 'Max', 'Mark', 'Mary', 'Anna', 'Yo'))

