class DoubleEndedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1


    def insertFront(self, value):
        if self.isFull():
            return "Full"

        if self.isEmpty():
            self.front = 0

        self.front = (self.front - 1 + self.capacity) % self.capacity

        self.queue[self.front] = value


    def insertRear(self, value):
        if self.isFull():
            return "Full"

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = value


    def deleteFront(self):
        if self.isEmpty():
            return "Empty"

        value = self.queue[self.front]
        self.queue[self.front] = None
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        else:
            self.front = (self.front+1) % self.capacity

        return value


    def deleteRear(self):
        if self.isEmpty():
            return "Empty"

        value = self.queue[self.rear]
        self.queue[self.rear] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity

        return value


    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front


    def isEmpty(self):
        return self.front == -1


    def size(self):
        if self.isEmpty():
            return 0

        return (self.rear - self.front + self.capacity) % self.capacity + 1


    def display(self):
        if self.isEmpty():
            return "Empty"

        i = self.front
        print("Queue:", end=" ")

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.capacity

        print()
            



obj = DoubleEndedQueue(6)

obj.insertFront(3)
obj.insertFront(1)
obj.insertFront(4)

obj.insertRear(7)
obj.insertRear(4)
obj.insertRear(9)

obj.display()

print(obj.isFull())
print(obj.isEmpty())

obj.deleteFront()
obj.deleteRear()

obj.display()


'''

Operation           Formula

Insert Front	    front = (front - 1 + N) % N
Insert Rear	        rear = (rear + 1) % N
Delete Front	    front = (front + 1) % N
Delete Rear	        rear = (rear - 1 + N) % N

'''