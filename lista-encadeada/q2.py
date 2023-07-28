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
        return self.head == None

    def add(self, item):
        if not self.search(item):
            temp = Node(item)
            if self.head is None:
                self.head = temp
            else:
                current = self.head
                while current.getNext() is not None:
                    current = current.getNext()
                current.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def __str__(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.getData()))
            current = current.getNext()
        return ' -> '.join(elements)

entrada = input().strip().split()

lista = UnorderedList()
for number in entrada:
    lista.add(int(number))

print(lista)
