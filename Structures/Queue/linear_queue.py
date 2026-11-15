class LinearQueue:
    def __init__(self):
        self.queue = []


    def enqueue(self, value):
        self.queue.append(value)


    def dequeue(self):
        if not self.queue:
            return "Empty"
        
        return self.queue.pop(0)


    def front(self):
        if not self.queue:
            return "Empty"
        
        return self.queue[0]


    def isEmpty(self):
        return len(self.queue) == 0


    def size(self):
        return len(self.queue)


    def display(self):
        if not self.queue:
            return "Empty"

        print("Queue:",*self.queue)



q = LinearQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()