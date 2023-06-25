# n = int(input())
# for i in range(n):
#     strlist = input()
#     for i in range(len(strlist)):
#         if i % 2 == 0:
#             print(strlist[i], end="")
#     print(" ", end="")
#     for i in range(len(strlist)):
#         if i % 2 != 0:
#             print(strlist[i], end="")
#     print()

# num_test_cases = int(input())

# for i in range(num_test_cases):
#     test_string = input()
#     even_string_characters = ''
#     odd_string_characters = ''

#     for j in range(len(test_string)):
#         if j % 2 == 0:
#             even_string_characters += test_string[j]
#         else:
#             odd_string_characters += test_string[j]

#     print('{} {}'.format(even_string_characters, odd_string_characters))

number = int(input())

for i in range(number):
    name = input()

    odd = ''
    even = ''

    for j in range(len(name)):

        if j % 2 == 0:
            odd += name[j]
        else:
            even += name[j]

    print('{} {}'.format(odd, even))
