def solution(nums, target):
    nums_d = {}
    for p1 in range(len(nums)):
        p2 = 0
        try:
            p2 = nums_d[nums[p1]]
        except KeyError:
            find = target - nums[p1]
            nums_d[find] = p1
            continue

        return [p2, p1]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    t = int(input())
    print(solution(nums, t)) 
