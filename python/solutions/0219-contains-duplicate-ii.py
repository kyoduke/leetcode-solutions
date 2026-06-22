import unittest


def contains_nearby_duplicate(nums: list[int], comparator: int) -> bool:
    seen = {}

    for index, value in enumerate(nums):
        if value in seen and abs(index - seen[value]) <= comparator:
            return True
        else:
            seen[value] = index

    return False


class TestContainsNearbyDuplicate(unittest.TestCase):

    def test_1(self):
        self.assertEqual(False, contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))

    def test_2(self):
        self.assertEqual(
            True,
            contains_nearby_duplicate([1, 0, 1, 1], 1),
        )
