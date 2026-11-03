nums = [1,2,54,23,12,43,12,43]

def selection_sort(nums: list[int]):
    n = len(nums)

    for i in range(n):
        minimum_index = i

        for j in range(i+1, n):
            if nums[j] < nums[minimum_index]:
                minimum_index = j

        nums[i], nums[minimum_index] = nums[minimum_index], nums[i]


selection_sort(nums)

for num in nums:
    print(num, end=" ")