import re
N = int(input())
for _ in range(N):
    try:
        S = input()
    except:
        break
    found = re.match(r"[^\W_]{10}", S)
    if found:
        if len(re.findall(r"\d", S)) < 3 or len(re.findall(r"[A-Z]", S)) < 2 or len(S) > len(set(S)):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")


N = int(input())
for _ in range(N):
    S = input()
    found = re.search(r"^[456]\d{3}(-?)(\d{4}\1){2}\d{4}$", S)
    if found:
        # NOT have 4 consecutive repeated digits
        found = re.search(r"(\d)-?(\1-?){3}", S)
        if found:
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
