cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    # Map and Lambda Function in Python - Hacker Rank Solution START
    storage = [0, 1]
    for i in range(2, n):
        storage.append(storage[i-1] + storage[i-2])
    return(storage[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))