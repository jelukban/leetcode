# 232. Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0
