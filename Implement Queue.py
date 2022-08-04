class queue:
    def __init__(self):
        self.queue_ds = []
        self.Front = -1
        self.Rear = -1

    def enqueue(self, val):
        self.queue_ds.append(val)
        if self.Front == -1:
            self.Front += 1
            self.Rear += 1
            print(val, ' is successfully inserted')
        else:
            self.Rear += 1
            print(val, ' is successfully inserted')

    def dequeue(self):
        if len(self.queue_ds) == 0:
            print('Queue is empty')
            return
        else:
            temp = self.queue_ds.pop(self.Front)
            print('Deleted item = ', temp)
            self.Rear -= 1
            if len(self.queue_ds) == 0:
                self.Front = -1
                self.Rear = -1
            return

    def display(self):
        if len(self.queue_ds) == 0:
            print('Queue empty')
            return
    print('The contents of Queue are')
    if self.Front == self.Rear:
        print(self.queue_ds[self.Front], '<== Front <== Rear')
        return
    print(self.queue_ds[self.Front], '<== FRONT', i=self.Front + 1)
    i = self.Front + 1
    while i < self.Raer:
        print(self.queue_ds[i])
        i += 1
    print(self.queue_ds[self.Rear], '<== REAR')


a = queue()
while True:
    print('*****************************')
    option = int(input('Enter your choice\n1:Insert\n2:Delete\n3:Display\n4:

    if option == 1:
        value = int(input('Enter the value you want to add: '))
        a.enqueue(value)
        continue
    elif option == 2:
        a.dequeue()
        continue
    elif option == 3:
        a.display()
        continue
    elif option == 4:
        print('Exiting')
        break
    else:
        print('Wrong option')
