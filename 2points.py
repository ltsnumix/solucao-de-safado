def find_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return(nums[left], nums[right])
        elif sum < target:
            left += 1
        else:
            right -= 1
nums = list(map(int, input().split()))
target = int(input())
result = find_pair(nums, target)
print(f"Found pair {result}"if result else "Num foi kk")
