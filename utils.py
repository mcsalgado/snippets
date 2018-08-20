cat = ''.join


def prod(ns):
    ret = 1
    for n in ns:
        ret *= n
    return ret


def clamp(n, minimum, maximum):
    ret = max(minimum, min(n, maximum))
    return ret


# NOTE(mcsalgado): the python docs has a recipe with a similar implementation
# of this function called 'grouper'
# https://docs.python.org/3.7/library/itertools.html#itertools-recipes
def partition(iterable, size):
    iterator = iter(iterable)
    while True:
        ret = ()
        for _ in range(size):
            try:
                ret += (next(iterator),)
            except StopIteration:
                if ret != ():
                    yield ret
                return
        yield ret


def manhattan_neighbors(coordinate):
    x, y = coordinate

    n = (x-1, y)
    e = (x, y+1)
    s = (x+1, y)
    w = (x, y-1)

    ret = (n, e, s, w)
    return ret


def chebyshev_neighbors(coordinate):
    x, y = coordinate

    n = (x-1, y)
    ne = (x-1, y+1)
    e = (x, y+1)
    se = (x+1, y+1)
    s = (x+1, y)
    sw = (x+1, y-1)
    w = (x, y-1)
    nw = (x-1, y-1)

    ret = (n, ne, e, se, s, sw, w, nw)
    return ret
