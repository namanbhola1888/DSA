class MonotonicSubarray:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        increasing_subarray = 1
        decreasing_subarray = 1
        maximum = 1

        for i in range(n-1):
            if nums[i+1] > nums[i]:
                increasing_subarray += 1
                decreasing_subarray = 1

            elif nums[i+1] < nums[i]:
                decreasing_subarray += 1
                increasing_subarray = 1

            else:
                increasing_subarray = 1
                decreasing_subarray = 1

            maximum = max(maximum, increasing_subarray, decreasing_subarray)

        return maximum



nums = [1,4,3,3,2]

obj = MonotonicSubarray()
print(obj.longestMonotonicSubarray(nums))