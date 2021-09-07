n = int(input())
numbers = list(map(int,input().split()))
count = 0
count_palindrome = 0
for element in numbers:
    if element > 0:
        count += 1
for i in range(len(numbers)):
    string = str(numbers[i])
    counts = 0
    for j in range(len(string)//2):
        if string[j] == string[-1-j]:
            counts += 1
    if counts == len(string)//2:
        count_palindrome += 1
if count_palindrome > 0 and count ==len(numbers):
    print(True)
else:
    print(False)