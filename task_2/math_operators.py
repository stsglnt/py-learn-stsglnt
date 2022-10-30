def get_sum(a, b, c):
    if not isinstance(a, int):
        raise TypeError(f'Argument cannot be {type(a)}')
    elif not isinstance(b, int):
        raise TypeError(f'Argument cannot be {type(a)}')
    elif not isinstance(c, int):
        raise TypeError(f'Argument cannot be {type(a)}')
    else:
        return a + b + c

