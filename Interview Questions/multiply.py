def find(n):
    if n < 10:
        print(n+10)
        return
        
    f = []
    for i in range(9, 1, -1):
        while n % i == 0:
            n = n/i
            f.append(i)
    if n > 10:
        print("Not Possible")
        return
    f.reverse()
    s = [str(i) for i in f]
    s = "".join(s)
    print(s)

n = int(input())
find(n)
