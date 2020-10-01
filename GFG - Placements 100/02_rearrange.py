# l = [8, 5, 0, 10, 0]
l = [10, 5, 0, 0, 8, 0, 9, 0]
def naive():
    for i in range(len(l)):
        if l[i] == 0:
            for j in range(i + 1, len(l)):
                if l[j] != 0:
                    l[i], l[j] = l[j], l[i]
                    break
            else:
                break

def best():
    count = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[i], l[count] = l[count], l[i]
            count += 1


best()
# naive()
print(l)
