from math import gcd

class MaxSubarrayEqualProduct:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = (l * nums[j]) // gcd(l, nums[j])

                if prod == l*g:
                    ans = max(ans, j-i+1)

        return ans
    

nums = [2,3,4,5,6]

obj = MaxSubarrayEqualProduct()
print(obj.maxLength(nums))