class reverse_iter:

    def __init__(self, items):
        self.items = list(items)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.items:
            raise StopIteration

        return self.items.pop()

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

