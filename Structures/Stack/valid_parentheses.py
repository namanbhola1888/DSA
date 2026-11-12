st = "()(())"

def checkValidParentheses(st: str) -> bool:
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in st:
        if char in pairs.values():
            stack.append(char)

        else:
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


print(checkValidParentheses(st))
