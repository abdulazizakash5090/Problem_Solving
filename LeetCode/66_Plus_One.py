# digits = [9]
# for i in digits:
#     print(i, end="")
# onePlus = i+1
# print(onePlus)


# digits = [1, 2, 3]
# onePlus = 0  # Initialize 'onePlus' before the loop
# for i in digits:
#     print(i, end="")
#     onePlus = i + 1  # Increment 'i' by 1 and store it in 'onePlus'
# print(onePlus)


# my_interger = onePlus
# my_string = str(my_interger)

# digitss = [int(char) for char in my_string]

# print(digitss)


# def convert(list):

#     s = [str(i) for i in list]

#     res = int("".join(s))

#     return res


# list = [1, 2, 3]
# print(convert(list))


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:

#         for i in range(len(digits)-1, -1, -1):
#             if digits[i] == 9:
#                 digits[i] = 0
#             else:
#                 digits[i] = digits[i] + 1
#                 return digits
#         return [1] + digits


# class Solution:
#     def plusOne(self, digits):
#         strings = ""
#         for number in digits:
#             strings += str(number)

#         temp = str(int(strings)+1)

#         return [int(temp[i] for i in range(len(temp)))]


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         s = ''.join(map(str, digits))
#         x = int(s)+1
#         k = str(x)
#         p = [int(i) for i in k]
#         return p

digits = [1]
for i in range(len(digits)-1, -1, -1):
    # print(i, end='')
    if digits[i] == 9:
        digits[i] = 0
    else:
        digits[i] = digits[i] + 1
        print(digits)
print([1]+digits)


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits = digits[::-1]
#         one, i = 1, 0

#         while one:
#             if i < len(digits):
#                 if digits[i] == 9:
#                     digits[i] = 0
#                 else:
#                     digits[i] += 1
#                     one = 0
#             else:
#                 digits.append(1)
#             i += 1
#         return digits[::-1]
