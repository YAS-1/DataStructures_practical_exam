class StudentQueue:
    def __init__(self):
        self.data = []
        self.front = -1

    def enqueue(self,value):
        self.data.append(value)

    def dequeue(self):
        self.front = self.front + 1
        del self.data[self.front]

    def isEmpty(self):
        if len(self.data) == 0:
            print('Queuen is empty')
        else:
            print('There are students')

    def queue_size(self):
        print(len(self.data))
    
    def display(self):
            print(self.data)

StudentQueue = StudentQueue()
StudentQueue.enqueue('Jasper')
StudentQueue.enqueue('Robert')
StudentQueue.enqueue('Peter')
StudentQueue.enqueue('Roger')
StudentQueue.enqueue('Marvin')
        
StudentQueue.display()

StudentQueue.dequeue()

StudentQueue.display()

StudentQueue.isEmpty()

StudentQueue.queue_size()
