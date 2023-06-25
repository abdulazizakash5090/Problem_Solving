# name = input()

# if name == "Bond":
#     print("Welcome on board 007.")
# else:
#     # print(f"Good monning {name}")
#     print("Good morning " + name)


# name = input("Enter your name.")

# # if name.isalpha():
# #     print("Welcome on board 007")
# # else:
# #     print("not Match")

# if name.lower() == "bond":
#     print("Welcome on board 007")
# else:
#     print("Good morning" + name)


# def evens(i):
#     if i % 2 == 0:
#         return True
#     else:
#         return False


# print(evens(99))
# print(evens(98))

# def thedecimal(number):
#     if number % 1 == 0:
#         return "INTEGER"
#     else:
#         return "Not match"


# print(thedecimal(99.09))
# print(thedecimal(99.00))


treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "Canada": 36388, "Bulgaria": 24987,
               "France": 24436, "Greece": 24323, "United States": 23513, "Turkey": 11126, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}
# Type your answer here.


# def moretrees(dict):
#     lst = []
#     for i in dict:
#         if dict[i] > 20000:
#             lst.append(i)
#         else:
#             pass
#     return lst


# print(moretrees(treepersqkm))


# str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"


# # Type your answer here.

# def count_l(a):
#     c = 0
#     for i in a.split():
#         if "l" in i:
#             c = c + 1
#         else:
#             pass
#     return c


# print(count_l(str))


str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"


# Type your answer here.

# def count_l(a):
#     c = 0
#     for i in a.split():
#         if i[0].lower() == a:
#             c = c+1
#         else:
#             pass

#     return c


# print(count_l(str))

# x = 8
# y = 15

# if x > 3 or y % 2 == 0:
#     print("At least one of the conditions is satisfied.")
# if x < + 3 or y % 2 == 1:
#     print("Neither condition is satisfied.")

# age = int(input("Enter voters age:"))

# if age >= 18:
#     print("You can cast your vote!")
# else:
#     print("Sorry! You are not eligible to votte!")


# signal = input("What is a traffic signal? :").title()

# if signal == "Red":
#     print("Stop you car!")
# elif signal == "Yelow":
#     print("Wait your car!")
# else:
#     print("Unrecgonized singal")

name = input("Enter student name:")
clas = input("Enter class:")
section = input("Enter section:")
grade = input("Enter students grade:").upper()
print("--------------------")
print("Name:", name)
print("Class:", clas)
print("Section:", section)
if grade == "A":
    print("Grade: Outstanding!")
elif grade == "B":
    print("Grade: Excellent!")
elif grade == "C":
    print("Grade: Very Good!")
elif grade == "D":
    print("Grade: Good!")
elif grade == "E":
    print("Grade: Satisfactory!")
else:
    print("Unrecognized Grade!")
