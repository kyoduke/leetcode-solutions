from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    s = Solution()

    cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([0, 4, 5, 0, 3, 6], True),
        ([1000000000, 1000000000, 11], True),
        ([1, 5, -2, -4, 0], False),
    ]
    for testcase, expected in cases:
        result = s.containsDuplicate(testcase)
        print(f"Expected: {result} --- Result: {expected}")
