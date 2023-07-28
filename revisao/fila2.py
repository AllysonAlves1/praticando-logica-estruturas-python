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
        print(self.items)

queue = Queue()

num_op = int(input())

fila = []
for _ in range(num_op):
    op = input().split()
    fila.append(op)

for op in fila:
    if op[0] == 'E':
        queue.enqueue(int(op[1]))
    elif op[0] == 'D':
        if not queue.isEmpty():
            queue.dequeue()

queue.printQueue()