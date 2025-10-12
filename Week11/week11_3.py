
def add(a, b):
    """
    sum of a and b.

    >>> add(2, 3)
    5
    >>> add(-1, 5)
    4
    """
    return a + b


def subtract(a, b):
    """
    difference between a and b.

    >>> subtract(10, 5)
    5
    >>> subtract(3, 8)
    -5
    """
    return a - b


def divide(a, b):
    """
    division of a by b.

    >>> divide(10, 2)
    5.0
    >>> divide(5, 2)
    2.5
    >>> divide(5, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return a / b


def mod(a, b):
    """
    Returns the remainder when a is divided by b.

    >>> mod(10, 3)
    1
    >>> mod(8, 4)
    0
    >>> mod(5, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: integer modulo by zero
    """
    return a % b




if __name__ == "__main__":
    import doctest
    print("Running doctests...")
    doctest.testmod(verbose=True)


#python -m doctest -v week11_3.py

