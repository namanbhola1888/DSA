class MinMovesII:
    def minMoves2(self, nums:list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]

        moves=0
        for num in nums:
            moves += abs(num - median)

        return moves

nums = [1, 10, 2, 9]

obj = MinMovesII()
print(obj.minMoves2(nums))