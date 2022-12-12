class dictionary_iter:

    def __init__(self, kwargs):
        self.kwargs = kwargs
        self.result = [(key, value) for key, value in kwargs.items()]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.result:
            raise StopIteration

        return self.result.pop(0)

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
