import doctest


# assert
def divide(x, y):
    assert y != 0
    return x / y


result = divide(6, 1)

print(result)  # AssertionError: Divisão por zero!


# doctest
def square(x):
    '''
    Retorna o quadrado de um número.
    Exemplos:

    >>> square(3)
    9

    >>> square(-2)
    4

    >>> square(0)
    0
    '''

    return x * x


doctest.testmod()
