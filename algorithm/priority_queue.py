class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def push(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print('IndexError Occur')
            exit()


if __name__ == '__main__':
    myQueue = PriorityQueue()
    if myQueue.isEmpty():
        print(f'myQueue is Empty')
    myQueue.push(12)
    myQueue.push(1)
    myQueue.push(14)
    myQueue.push(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.pop())
        