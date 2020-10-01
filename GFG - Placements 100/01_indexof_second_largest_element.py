def largest(l):
    m = l[0]
    index = 0
    for i in range(1, len(l)):
        if l[i] > m:
            m = l[i]
            index = i

    return index


# l = list(map(int, input().split()))
l = [10, 5, 8, 20, 12]

i = largest(l)
l[0], l[i] = l[i], l[0]
i = largest(l[1:])
print(i + 1)