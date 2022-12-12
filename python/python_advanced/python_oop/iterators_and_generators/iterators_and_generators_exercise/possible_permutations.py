import itertools

def possible_permutations(some_list):

    result = [list(nums) for nums in itertools.permutations(some_list)]

    while result:
        yield result.pop(0)

[print(n) for n in possible_permutations([1, 2, 3])]
