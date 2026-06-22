class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if len(mat) == 1:
            return mat[0][0]

        result = 0
        intersection = len(mat) // 2 if len(mat) % 2 != 0 else None
        for i, arr in enumerate(mat):

            result += arr[i]
            result += arr[-i - 1]

        if intersection:
            result -= mat[intersection][intersection]

        return result


if __name__ == "__main__":
    sol = Solution()
    result_1 = sol.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    result_2 = sol.diagonalSum([[1, 2, 3, 5], [4, 5, 6, 2], [7, 8, 9, 7], [7, 8, 9, 5]])
    result_3 = sol.diagonalSum([[7, 3, 1, 9], [3, 4, 6, 9], [6, 9, 6, 6], [9, 5, 8, 5]])

    assert result_1 == 25, f"Error test 1, Expected {25} got {result_1}"
    assert result_2 == 46, f"Error test 1, Expected {46} got {result_2}"
    assert result_3 == 55, f"Error test 1, Expected {55} got {result_3}"
