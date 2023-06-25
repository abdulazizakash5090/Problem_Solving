def average(array):
    # your code goes here
    h_set = set(array)
    return sum(h_set)/len(h_set)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
