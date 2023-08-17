# def isValid(s):
#     if s == "()":
#         return True
#     elif s == "[]":
#         return True
#     elif s == "{}":
#         return False
#     elif s == "()[]{}":
#         return True
#     else:
#         return False


# s = "()[]{}"
# ans = isValid(s)
# print(ans)

# Stack implementation in python


# Creating a stack
# def create_stack():
#     stack = []
#     return stack


# # Creating an empty stack
# def check_empty(stack):
#     return len(stack) == 0


# # Adding items into the stack
# def push(stack, item):
#     stack.append(item)
#     print("pushed item: " + item)


# # Removing an element from the stack
# def pop(stack):
#     if (check_empty(stack)):
#         return "stack is empty"

#     return stack.pop()


# stack = create_stack()
# push(stack, str(()))
# push(stack, str([]))
# push(stack, str({}))
# push(stack, str(4))
# print("popped item: " + pop(stack))
# print("stack after popping an element: " + str(stack))


# s = "()[]{}"

# if s in stack:
#     print("True")
# else:
#     print("False")

# s = "(]"

# if s in "()[]{}":
#     print("True")
# else:
#     print("False")


# def check_and_pop(value, stack):

#     if value in stack:
#         stack.pop()
#         return True
#     return False


# if __name__ == "__main__":
#     values = "()[]{}"
#     stack = []
#     for value in values:
#         stack.append(value)
#         if check_and_pop(value, stack):
#             print(f"Popped {value}")
#     print(stack)


# value = "()"

# ans = check_and_pop(value, stack)

# values = "()[]{}"
# stack = []
# for value in values:
#     stack.append(value)
#     print(f"Popped {value}")
# print(stack)

class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0
