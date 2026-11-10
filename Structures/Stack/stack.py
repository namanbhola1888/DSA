class Stack:
    def __init__(self):
        self.stack = []


    def push(self, data):
        self.stack.append(data)


    def pop(self):
        if self.isEmpty():
            return "Empty"

        self.stack.pop()


    def peek(self):
        if self.isEmpty():
            return "Empty"

        return self.stack[-1]


    def isEmpty(self):
        return len(self.stack) == 0


    def size(self):
        return len(self.stack)



s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.pop())    
print(s.peek())   
print(s.size())  
print(s.isEmpty())   