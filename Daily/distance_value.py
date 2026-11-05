class DistanceValueOfArray:

    # Brute Force Approach
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0

        for num1 in arr1:
            flag = False

            for num2 in arr2:
                if abs(num1 - num2) > d:
                    flag = True
                else:
                    flag = False
                    break

            if flag: 
                count+=1

        return count
    

list1 = [4,5,8]
list2 = [10,9,1,8]
d = 2

obj = DistanceValueOfArray()
print(obj.findTheDistanceValue(list1, list2, d))