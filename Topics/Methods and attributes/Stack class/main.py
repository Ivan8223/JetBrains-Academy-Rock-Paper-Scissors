class Stack:
    def __init__(self):
        self.array = []

    def push(self, el):
        self.array.append(el)

    def pop(self):
        return self.array.pop()

    def peek(self):
        return self.array[-1]

    def is_empty(self):
        return not self.array
