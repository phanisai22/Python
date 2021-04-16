n = int(input())
li = list(map(int, input().split()))

avg = sum(li) // n
s = 0
for item in li:
    if item > avg:
        s += (item - avg)

print(s)