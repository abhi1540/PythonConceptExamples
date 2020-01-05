class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def is_empty(self):
        return (self.inbox.is_empty() and self.outbox.is_empty())

    def enqueue(self, data):
        self.inbox.push(data)

    def dequeue(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                popped = self.inbox.pop()
                self.outbox.push(popped)
        return self.outbox.pop()


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


class Product(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

