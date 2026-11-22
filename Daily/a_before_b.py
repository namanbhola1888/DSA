class ABeforeB:
    def checkString(self, s: str) -> bool:
        n = len(s)

        for i in range(n-1):
            if s[i] == 'b' and s[i+1] == 'a':
                return False

        return True 


s = "aaabbb"

obj = ABeforeB()
print(obj.checkString(s))