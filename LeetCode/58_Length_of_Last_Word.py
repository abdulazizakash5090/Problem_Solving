s = "luffy is still joyboy"

last = s.split()[-1]
print(len(last))


def lengthOfLastWord(s):
    stripped = s.strip()
    strList = stripped.split("")
    lastWord = stripped[-1]
    return len(lastWord)


def lengthOfLastWord(s):
    s = s.strip()
    length = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            break
        length += 1

    return length


def lengthOfLastWord(s):
    l = s.split()
    return len(l[-1])
