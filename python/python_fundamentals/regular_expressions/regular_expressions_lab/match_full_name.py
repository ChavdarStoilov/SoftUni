import re

class MatchingNames:

    def __init__(self, names):
        self.exception = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", names)


    def __repr__(self):
        return f"{' '.join(self.exception)}"

some_names = input()
name = MatchingNames(some_names)

print(name)