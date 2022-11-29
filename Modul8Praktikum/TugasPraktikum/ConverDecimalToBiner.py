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
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
s1 = Stack()

def ConvertDecToBin(decNum):
    while decNum!=0:
        newNum = decNum%2
        decNum = decNum//2
        s1.push(newNum)
    while s1.size() !=0:
        a = s1.pop()
    return a

print(ConvertDecToBin(42))