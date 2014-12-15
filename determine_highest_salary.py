# have a tree showing structure of company. Some people have zero children, some have some number. Find max salary
# assumes class of person, with attributes of 1) list of children and 2) salary (which is an integer)


def high_salary(person):
    salaries = [person.salary]
    for child in person.children:
        salaries.append(high_salary(child))
    return max(salaries)

def hi_salary(person):
    if person.children == []:
        person
    else:
        max_salary_person = person
        for child in person.children:
            if max_salary_person.salary < hi_salary(child).salary:
                max_salary_person = child

        return max_salary_person
