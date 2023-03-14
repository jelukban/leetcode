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


# 20. Valid Parentheses
def isValid(self, s: str) -> bool:
    parentheses = []
    balanced = True
    idx = 0

    while idx < len(s) and balanced:
        symbol = s[idx]

        if symbol in '([{':
            parentheses.append(symbol)
        elif parentheses and symbol in ')' and parentheses[-1] == '(':
            parentheses.pop()
        elif parentheses and symbol in ']' and parentheses[-1] == '[':
            parentheses.pop()
        elif parentheses and symbol in '}' and parentheses[-1] == '{':
            parentheses.pop()
        else:
            balanced = False

        idx += 1

    if balanced and len(parentheses) == 0:
        return True
    else:
        return False
