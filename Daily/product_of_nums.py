class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]


    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)


    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        
        return self.prefix[-1] // self.prefix[-k-1]



obj = ProductOfNumbers()

obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)

print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
print(obj.getProduct(2))