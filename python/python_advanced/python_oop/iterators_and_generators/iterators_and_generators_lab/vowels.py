class vowels:
    VOWELS = ("AEIOUyaeiouy")

    def __init__(self, text):
        self.text = [char for char in text if char in self.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.text:
            raise StopIteration

        char = self.text.pop(0)

        return char

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
