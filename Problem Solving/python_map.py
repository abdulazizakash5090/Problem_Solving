# n = int(input())
# arr = map(int, input().split())

# scores = list(arr)

# scores.sort()
# first = None
# second = None

# for score in scores:
#     if first < score:
#         second = first
#         first = score
# print(second)

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here

    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)

    tip = meal_cost / 100 * 20
    tax = tax_percent / 100 * 12

    total_cost = meal_cost + tip + tax


print(solve())
