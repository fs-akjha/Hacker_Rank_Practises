if __name__ == '__main__':
    N = int(input())
    
    output=[]
    for i in range(0,N):
        it=input().split()
        if it[0]=="print":
            print(output)
        elif it[0]=="insert":
            output.insert(int(it[1]),int(it[2]))
        elif it[0]=="remove":
            output.remove(int(it[1]))
        elif it[0]=="append":
            output.append(int(it[1]))
        elif it[0]=="pop":
            output.pop()
        elif it[0]=="sort":
            output.sort()
        else:
            output.reverse()