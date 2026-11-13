class Stack:
    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, data):
        self.stack.append(data)

        if not self.minStack:
            self.minStack.append(data)
        else:
            self.minStack.append(
                min(data, self.minStack[-1])
            )


    def pop(self):
        if self.isEmpty():
            return "Empty"

        self.stack.pop()


    def peek(self):
        if self.stack:
            self.stack.pop()
            self.minStack.pop()


    def isEmpty(self):
        return len(self.stack) == 0


    def size(self):
        return len(self.stack)


    def getTop(self):
        if not self.stack:
            return -1

        return self.stack[-1]


    def getMin(self):
        if not self.minStack:
            return -1
        
        return self.minStack[-1]



s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.pop())    
print(s.peek())   
print(s.size())  
print(s.isEmpty())   