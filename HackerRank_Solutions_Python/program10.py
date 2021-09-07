if __name__ == '__main__':
    all_data=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        all_data.append([name,score])

score_data=[score for name,score in all_data]
nd_highest=sorted(set(score_data))[1]
names_with_nd_highest='\n'.join(sorted([name for name,score in all_data if score==nd_highest]))
print(names_with_nd_highest)