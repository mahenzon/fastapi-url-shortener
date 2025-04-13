import random
from unittest import TestCase


def total(a: int, b: int) -> int:
    return a + b


class TotalTestCase(TestCase):
    def test_total(self) -> None:
        num_a = random.randint(1, 100)
        num_b = random.randint(1, 100)
        result = total(num_a, num_b)
        expected_result = num_a + num_b
        self.assertEqual(expected_result, result)
