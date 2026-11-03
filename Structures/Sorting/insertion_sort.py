nums = [1,2,54,23,12,43,12,43]

def insertion_sort(nums: list[int]):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i-1

        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key


insertion_sort(nums)

print(nums)