nums = [1,23,42,12,43,12]
target = 12

def linearSearch(nums: list[int], target: int) -> int:
    index = 0

    for num in nums:
        if num == target:
            return index
        index+=1

    else:
        return -1

print(linearSearch(nums, target))