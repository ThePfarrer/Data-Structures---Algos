class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        return self.data.pop(0)
    
    def read(self):
        return [] if  len(self.data) == 0 else self.data[0]