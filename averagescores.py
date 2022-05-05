n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
def percentage(query_name):
    scores = sum(student_marks[query_name])/n
    return scores