class Queue:

    def __init__(self):
        self.items = []
        self.next_ticket_number = 1

    def enqueue(self, item):
        ticket_number = self.next_ticket_number

        ticket = {
            "ticket_number": ticket_number,
            "customer_name": item
        }
        self.items.append(ticket)
        self.next_ticket_number += 1

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
    