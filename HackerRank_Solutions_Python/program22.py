n1 = int(input())
s1 = set(map(int, input().split()))

n2 = int(input())
s2 = set(map(int, input().split()))

union_data=s1.union(s2)
length_of_union_data=len(union_data)
print(length_of_union_data)