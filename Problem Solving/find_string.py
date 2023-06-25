def count_substring(string, sub_string):
    c = 0
    l = len(sub_string)
    for i in range(len(sub_string)):
        s = string[i:i+1]
        if s == sub_string:
            c += 1
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
