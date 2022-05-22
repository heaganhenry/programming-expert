# Write a function that accepts a list of lists that contain the name, age and salary of specific employees and also accepts a string representing the key to sort employees by.
# Your function should return a new list that contains the lists representing each employee sorted in ascending order by the given key.

def sort_by_first(item):
    return item[0]

def sort_by_second(item):
    return item[1]

def sort_by_third(item):
    return item[2]

def sort_employees(employees, sort_by):
    result = []
    if sort_by == "name":
       result = sorted(employees, key=sort_by_first)
    elif sort_by == "age":
       result = sorted(employees, key=sort_by_second)
    elif sort_by == "salary":
        result = sorted(employees, key=sort_by_third)

    return result