class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def __str__(self):
        current = self.head
        elements = []
        while current is not None:
            if current.getData() % 2 == 0:
                elements.append(str(current.getData()))
            current = current.getNext()
        return ' -> '.join(elements)


entrada = input().strip().split()

lista = UnorderedList()
for number in reversed(entrada):
    lista.add(int(number))

print(lista)
