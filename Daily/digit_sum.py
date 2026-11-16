class DigitSum:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k):
                temp = s[i: i+k]

                digit_sum = 0

                for digit in temp:
                    digit_sum += int(digit)

                ans += str(digit_sum)

            s = ans

        return s


s = "11111222223"
k = 3

obj = DigitSum()
print(obj.digitSum(s, k))