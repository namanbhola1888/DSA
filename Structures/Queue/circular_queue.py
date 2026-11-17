class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1


    def enqueue(self, value):
        if self.isFull():
            return "Full"

        if self.isEmpty():
            self.front = 0

        self.rear = (self.rear+1) % self.capacity

        self.queue[self.rear] = value


    def dequeue(self):
        if self.isFull():
            return "Full"

        value = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        else:
            self.front = (self.front+1) % self.capacity
    
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
        if not self.queue:
            return "Empty"

        i = self.front
        print("Queue:", end=" ")

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.capacity

        print()



obj = CircularQueue(5)

obj.enqueue(2)
obj.enqueue(5)
obj.enqueue(1)
obj.display()

obj.dequeue()
obj.display()

obj.isEmpty()
obj.isFull()
obj.size()