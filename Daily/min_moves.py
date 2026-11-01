class MinMoves:
    def min_moves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums)*min(nums)


nums = [1,2,3]

obj = MinMoves()
print(obj.min_moves(nums))