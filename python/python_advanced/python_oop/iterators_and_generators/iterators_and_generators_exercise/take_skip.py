class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration

        result = self.start
        self.start += self.step
        self.count -= 1

        return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
