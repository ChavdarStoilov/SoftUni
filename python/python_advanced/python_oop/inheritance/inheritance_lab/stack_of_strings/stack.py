class Stack:

    def __init__(self, data = []):
        self.data = data

    def push(self, element):

        self.data.append(element)

    def pop(self):

        if self.data:
            return self.data.pop()

    def top(self):

        if self.data:
            return self.data[-1]

    def is_empty(self):

        if self.data:
            return False

        return True

    def __str__(self):
        return f'[{", ".join(reversed([str(i) for i in self.data]))}]'


stack = Stack()
stack.pop()
stack.push("apple")
stack.push("carrot")
print(stack)
stack.pop()
stack.push("cucumber")
print(stack)
print(stack.is_empty())

