import doctest
import unittest


# assert
def sum_numbers_assert(numbers):
    assert sum([1, 2, 3, 4]) == 10
    assert sum([-1, 0, 1]) == 0
    assert sum([]) == 0
    return sum(numbers)


teste = sum_numbers_assert([1, 2, 3, 5])  
print(teste)


# doctest
def sum_numbers_doctest(numbers):
    '''
    Soma os números em uma lista.
    Exemplos:

    >>> sum_numbers_assert([1, 2, 3, 4])
    10

    >>> sum_numbers_assert([-1, 0, 1])
    0

    >>> sum_numbers_assert([])
    0
    '''

    return sum(numbers)


if __name__ == '__main__':
    doctest.testmod()


# unittest
def sum_numbers_unit(numbers):
    return sum(numbers)


class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers_positive(self):
        self.assertEqual(sum_numbers_unit([1, 2, 3, 4]), 10)

    def test_sum_numbers_mixed(self):
        self.assertEqual(sum_numbers_unit([-1, 0, 1]), 0)

    def test_sum_numbers_empty(self):
        self.assertEqual(sum_numbers_unit([]), 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
