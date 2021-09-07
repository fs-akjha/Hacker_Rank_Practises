if __name__ == '__main__':
    all_data=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        all_data.append([name,score])

second_highest=sorted(set([score for name, score in all_data]))[1]
print('\n'.join(sorted([name for name, score in all_data if score == second_highest])))