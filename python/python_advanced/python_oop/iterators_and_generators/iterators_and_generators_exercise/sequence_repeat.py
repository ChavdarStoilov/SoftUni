class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.sequence_chars = [char for char in self.sequence]
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.number == 0:
            raise StopIteration

        if self.counter == len(self.sequence):
            self.counter = 0

        result = self.sequence_chars[self.counter]
        self.counter += 1
        self.number -= 1

        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
