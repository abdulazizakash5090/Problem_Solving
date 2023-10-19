# binary_string = "101010"
# decimal_integer = int(binary_string, 2)
# print(decimal_integer)

# x = bin(11)
# y = bin(1)

# z = x + y
# print(z)

# Python3 code to demonstrate working of
# Converting String to binary
# Using join() + ord() + format()

# initializing string
# test_str = "11"

# # printing original string
# print("The original string is : " + str(test_str))

# # using join() + ord() + format()
# # Converting String to binary
# res = ''.join(format(ord(i), '08b') for i in test_str)

# # printing result
# print("The string after binary conversion : " + str(res))

binary_string1 = '11'
binary_string2 = '1'

int1 = int(binary_string1, 2)
int2 = int(binary_string2, 2)

result_int = int1 + int2

result_binary_string = bin(result_int)[2:]

print(result_binary_string)


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2))[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2

        return ''.join(reversed(s))
