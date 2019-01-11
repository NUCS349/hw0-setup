import random

def test_sum_numbers():
    from code import sum_numbers
    for i in range(100):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        assert sum_numbers(x, y) == (x + y)

def test_multiply_numbers():
    from code import multiply_numbers
    for i in range(100):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        assert multiply_numbers(x, y) == (x * y)