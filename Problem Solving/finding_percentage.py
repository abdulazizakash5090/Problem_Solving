if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        # print(student_marks)
    query_name = input()

print("{:.2f}" .format((sum(student_marks[query_name]) / 3)))
