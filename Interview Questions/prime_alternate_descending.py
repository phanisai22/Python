n = int(input())


def is_prime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


count = 2

for i in range(n, 1, -1):
    if count == 12:
        break
    if is_prime(i):
        if count %2 == 0:
            print(i)
            count += 1
        else:
            count += 1
