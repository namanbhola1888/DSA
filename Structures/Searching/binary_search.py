nums = [1,2,3,4,5,6,7,8,9]
target = 4

def binarySearch(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return -1


print(binarySearch(nums, target))