class countdown_iterator:

    def __init__(self, counter):
        self.counter = counter

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter < 0:
            raise StopIteration

        result = self.counter
        self.counter -= 1

        return result

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
