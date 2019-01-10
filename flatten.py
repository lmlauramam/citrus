           
def flatten(array):
    for elem in array:
        if isinstance(elem, list):
            yield from flatten(elem)
        elif isinstance(elem, int):
            yield elem
        else:
            raise TypeError("Oops! that type is not supported.")

sample = [1, 2, [1, 2, [1, 2, 3 ],[4, 5, 5 ]], [6, [[[7, 2]]]]]

print (list(flatten(sample)))
