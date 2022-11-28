class store_results:

    def __init__(self):
        pass


    def __str__(self):
        return 'Function {func_name} was add called. Result: {func_result}'


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
