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

    def concatenando(self, lista):
        if self.isEmpty():
            self.head = lista.head
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(lista.head)

    def __str__(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.getData()))
            current = current.getNext()
        return ' -> '.join(elements)

entrada1 = input().strip().split()
entrada2 = input().strip().split()

lista1 = UnorderedList()
for number in reversed(entrada1):
    lista1.add(int(number))

lista2 = UnorderedList()
for number in reversed(entrada2):
    lista2.add(int(number))

lista1.concatenando(lista2)

print(lista1)
