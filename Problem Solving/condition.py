# user_input = int(input("enter a number:"))

# if user_input % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# age = int(input("enter your age :"))

# if age < 18:
#     print('you are too young to marry')
# elif age > 60:
#     print('you are too old for marry')
# else:
#     print("we will find a perfect match for you")

# name = input("Enter your name : ")
# age = int(input("Enter your age :"))
# marks = float(input("Enter your marks :"))

# if (age >= 17 and age <= 21 and marks > 80):
#     print(name+" is eligible")
# else:
#     print(name + " is not eligible")

# a = int(input("Enter first side : "))
# b = int(input("Enter second side : "))
# c = int(input("Enter third side : "))

# if (c == (a**2 + b**2)**(1/2)):
#     print("Triangle is right angled.")
# if (a == b or a == c or b == c):
#     print("Triangle is isoceles")
# else:
#     print("Triangle is not of known type")

ch = input("Enter your character : ")
ascii_value = ord(ch)
if (ascii_value >= 65 and ascii_value <= 90):
    print("Upper case letter")
elif (ascii_value >= 97 and ascii_value <= 122):
    print("Lower case letter")
else:
    print("Character is not an alphabet")
