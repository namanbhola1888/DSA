nums = [1,2,54,23,12,43,12,43]

def bubble_sort(nums: list[int]):
    n = len(nums)

    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


bubble_sort(nums)

for num in nums:
    print(num, end=" ")