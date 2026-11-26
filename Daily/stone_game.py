class StoneGame:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice_turn = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn

        return not alice_turn


n = 12

obj = StoneGame()
print(obj.canAliceWin(n))