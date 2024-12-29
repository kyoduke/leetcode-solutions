import unittest


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i


class TestTwoSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual([0, 1], two_sum([2, 7, 11, 15], 9))

    def test_2(self):
        self.assertEqual([1, 2], two_sum([3, 2, 4], 6))

    def test_3(self):
        self.assertEqual([0, 1], two_sum([3, 3], 6))

    def test_4(self):
        self.assertEqual([0, 2], two_sum([3, 2, 3], 6))
