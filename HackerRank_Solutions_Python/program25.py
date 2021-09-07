n1 = int(input())
s1 = set(map(int, input().split()))

n2 = int(input())
s2 = set(map(int, input().split()))

symmetric_difference_data=s1.symmetric_difference(s2)
length_of_symmetric_difference_data=len(symmetric_difference_data)
print(length_of_symmetric_difference_data)