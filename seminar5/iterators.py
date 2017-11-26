

def unique(iterable):
    unique_elements = set()

    for el in iterable:
        if el not in unique_elements:
            unique_elements.add(el)
            yield el


def transpose(iterable):
    # except for the case it=[[]]
    return map(iter, zip(*iterable))
