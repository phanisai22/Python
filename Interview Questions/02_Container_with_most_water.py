def container(height):
    g_area = 0
    j = len(height) - 1
    i = 0

    while i < j:
        a, b = height[i], height[j]
        area = min(a, b) * (j - i)
        g_area = max(area, g_area)
        if a > b:
            j -= 1
        else:
            i += 1
    return g_area

if __name__ == "__main__":
    height = list(map(int, input().split()))
    print(container(height))
