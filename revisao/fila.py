class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        for e in reversed(self.items):
            print(e, end=" ")
        print()

F1 = Queue()
F2 = Queue()

for x in input().split():
    F1.enqueue(int(x))
    
for x in input().split():
    F2.enqueue(int(x))

while not F2.isEmpty():
    F1.enqueue(F2.dequeue())

F1.printQueue()






