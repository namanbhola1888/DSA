nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

def nextGreaterElement(num1: list[int], num2: list[int]) -> list[int]:
    stack = []
    nge = {}

    for num in num2:
        while stack and num > stack[-1]:
            smaller = stack.pop()
            nge[smaller] = num

        stack.append(num)

    result = []

    for num in num1:
        result.append(nge.get(num, -1))

    return result


print(nextGreaterElement(nums1, nums2))