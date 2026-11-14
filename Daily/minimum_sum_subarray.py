class MinimumSumSubarray:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            s = 0

            for j in range(i, n):
                s += nums[j]
                length = j-i+1

                if l <= length <= r and s > 0:
                    ans = min(ans, s)

        return -1 if ans == float('inf') else ans


nums = [3, -2, 1, 4]
l = 2
r = 3

obj = MinimumSumSubarray()
print(obj.minimumSumSubarray(nums, l ,r))