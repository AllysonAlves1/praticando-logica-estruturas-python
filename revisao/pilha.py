class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
        
     def printStack(self):
        for e in self.items:
            print(e, end="->")
        print()

def inverte_palavras(texto):
    pilha = Stack()
    for i, c in enumerate(texto):
        if c == ' ' or c == '.':
            while not pilha.isEmpty():
                print(pilha.pop(), end='')
            if c == ' ':
                print(c, end='')
            elif i != len(texto)-1:
                print(end=' ')
        else:
            pilha.push(c)

texto = input()
inverte_palavras(texto)