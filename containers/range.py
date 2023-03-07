def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]

    '''
    if not c:
        if not b:
            i = 0
            prev = 0
            if a <= 0:
                return []
            while i < a:
                if i == 0:
                    i += 1
                    num = 0
                    yield num
                else:
                    i += 1
                    prev += 1
                    yield prev
        if b:
            i = 0
            num_iterations = b - a
            prev = 0
            curr = a
            while i < num_iterations:
                if i == 0:
                    num = a
                    i += 1
                    yield num
                else:
                    num = curr + 1
                    curr = curr + 1
                    i += 1
                    yield num
    if c:
        step = c
        i = 0
        num_iterations = (b - a) / c
        curr = a
        while i < num_iterations:
            if i == 0:
                num = a
                i += 1
                yield num
            else:
                num = curr + step
                curr = curr + step
                i += 1
                yield num
