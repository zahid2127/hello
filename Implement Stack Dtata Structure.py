class stack:
    def __init__(self, maxSize, tops):
        self.maxSize = maxSize
        self.tops = tops
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def push(self, value):
        if self.tops == self.maxSize:
            print('The stack is full')
        else:
            self.list.append(value)
            self.tops += 1
            print(value, "has been successfully added to the stack")

    def pop(self):
        if self.tops == -1:
            print('The stack is empty')
        else:
            print('Popped item = ', self.list.pop())
            self.tops = 1

    def display(self):
        if self.tops == -1:
            print('The stack is empty')
        else:
            print('Contents of the stack are')
            print(self.list)


tempStack = stack(3, -1)
tempStack.push(10)
tempStack.push(20)
tempStack.push(30)
tempStack.display()
tempStack.pop()
tempStack.display()