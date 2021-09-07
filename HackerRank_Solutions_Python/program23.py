n1 = int(input())
s1 = set(map(int, input().split()))

n2 = int(input())
s2 = set(map(int, input().split()))

intersection_data=s1.intersection(s2)
length_of_intersection_data=len(intersection_data)
print(length_of_intersection_data)