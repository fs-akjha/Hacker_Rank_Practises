n1 = int(input())
s1 = set(map(int, input().split()))

n2 = int(input())
s2 = set(map(int, input().split()))

difference_data=s1.difference(s2)
length_of_difference_data=len(difference_data)
print(length_of_difference_data)