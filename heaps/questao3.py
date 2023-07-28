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

def heapify(arr, n, i): 
    largest = i # set largest as root
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if (l < n and arr[i] < arr[l]): 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if (r < n and arr[largest] < arr[r]): 
        largest = r 
  
    # Change root, if needed 
    if (largest != i): 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root.
        # print("*", arr)
        heapify(arr, n, largest) 
  
# function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a heap. 
    for i in range(n-1, -1, -1):
        heapify(arr, n, i)


    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap
        # print(arr)
        heapify(arr, i, 0) 
    
    return arr
  
# Driver code to test above

numeros = list(map(int, input().split()))
sorted_list = heapSort(numeros)
stack = Stack()
for num in sorted_list:
    stack.push(num)
while not stack.isEmpty():
    print(stack.pop(), end=" ")