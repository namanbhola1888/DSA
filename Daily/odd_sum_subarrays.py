class OddSumSubarrays:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        prefix = 0
        even = 1
        odd = 0
        ans = 0

        for num in arr:
            prefix += num

            if prefix % 2 == 0:
                ans += odd
                even += 1

            else:
                ans += even
                odd += 1

        return ans % MOD


arr = [1, 3, 5]

obj = OddSumSubarrays()
print(obj.numOfSubarrays(arr))