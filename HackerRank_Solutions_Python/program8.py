if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    
total=0
for i in student_marks[query_name]:
    total=total+i

avg_score=float(round((total/3),2))
print(format(avg_score, '.2f'))