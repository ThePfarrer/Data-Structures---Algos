class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        return self.data.pop(0)

    def read(self):
        return [] if not self.data else self.data[0]
