class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty.")
            return

        customer = self.items.pop(0)
        return customer

    def peek(self):
        if self.is_empty():
            print("The queue is empty.")
            return

        customer = self.items[0]
        return customer

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    