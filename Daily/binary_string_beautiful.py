class StringBeautiful:
    def minChanges(self, s: str) -> int:
        changes = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                changes += 1

        return changes


s = "1001"

obj = StringBeautiful()
print(obj.minChanges(s))