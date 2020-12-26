# def trap(height):
#     t_water = 0
#     for p in range(len(height)):
#         left_p = right_p = p
#         max_left = max_right = 0

#         while left_p >= 0:
#             max_left = max(max_left, height[left_p])
#             left_p -= 1

#         while right_p < len(height):
#             max_right = max(max_right, height[right_p])
#             right_p += 1

#         cur_water = min(max_left, max_right) - height[p]
#         if cur_water > 0:
#             t_water += cur_water

#     return t_water

def trap(height):
    left = 0
    right = len(height) - 1
    total = r_max = l_max = 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= l_max:
                l_max = height[left]
            else:
                total += l_max - height[left]
            left += 1
        else:
            if height[right] >= r_max:
                r_max = height[right]
            else:
                total += r_max - height[right]
            right -= 1

    return total


if __name__ == "__main__":
    height = [4, 2, 0, 3, 2, 5]
    print(trap(height))
