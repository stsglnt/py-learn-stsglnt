def get_sum(a, b, c):
    if not isinstance(a, int):
        raise ValueError(f'Argument cannot be {type(a)}')
    elif not isinstance(b, int):
        raise ValueError(f'Argument cannot be {type(a)}')
    elif not isinstance(c, int):
        raise ValueError(f'Argument cannot be {type(a)}')
    else:
        return a + b + c

