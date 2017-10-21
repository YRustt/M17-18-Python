
def smart_function():
    i = 0
    while True:
        i += 1
        yield i


def smart_function_2(count=[0]):
    count[0] += 1
    return count[0]

