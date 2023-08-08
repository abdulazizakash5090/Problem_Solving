# import functools
# a = ("b", "g", "a", "d", "f", "c", "h", "e")

# x = sorted(a)
# print(x)


# a = ("h", "b", "a", "c", "f", "d", "e", "g")
# x = sorted(a, reverse=True)
# print(x)

# numbers = [4, 2, 12, 8]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)

# # take the second element for sort


# def take_second(elem):
#     return elem[1]


# # random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sorted_list = sorted(random, key=take_second)

# print('Sorted list:', sorted_list)


# # Nested list of student's info in a Science Olympiad
# # List elements: (Student's Name, Marks out of 100 , Age)
# participant_list = [
#     ('Alison', 50, 18),
#     ('Terence', 75, 12),
#     ('David', 75, 20),
#     ('Jimmy', 90, 22),
#     ('John', 45, 12)
# ]


# def sorter(item):
#     error = 100 - item[1]
#     age = item[2]
#     return (error, age)


# sorted_list = sorted(participant_list, key=sorted)
# print(sorted_list)

# sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
# print(sorted_list)

# print(sorted([4, 1, 3, 2]))


# x = [2, 8, 1, 4, 6, 3, 7]

# print("Sorted List returned :", sorted(x))

# print("Reverse sort :", sorted(x, reverse=True))

# print("\nOriginal list not modified :", x)


# test_string = "geekforgeeks"

# print("The original string : " + str(test_string))

# res = ''.join(sorted(test_string, reverse=True))

# print("String after reverse sorting :" + str(res))

# test_string = "geekforgeeks"

# print("The original string : " + str(test_string))

# res = functools.reduce(lambda x, y: x+y, sorted(test_string, reverse=True))
# print("String after reverse sorting : " + str(res))


# L = ["cccc", "b", "dd", "aaa"]
# print("Normal sort :", sorted(L))
# print("Sort with len :", sorted(L, key=len))


# def func(x):
#     return x % 7


# L = [15, 3, 11, 7]

# print("Normal sort :", sorted(L))
# print("Sorted with key:", sorted(L, key=func))

my_tuples = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
sorted_tuples = sorted(my_tuples, key=lambda x: x[1])

print(sorted_tuples)

students = [
    {'name': 'John', 'age': 20},
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 22}
]

sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}',age={self.age})"


people = [
    Person('John', 25),
    Person('Alice', 18),
    Person('Bob', 30)
]

sorted_people = sorted(people, key=lambda x: x.age)
print(sorted_people)
