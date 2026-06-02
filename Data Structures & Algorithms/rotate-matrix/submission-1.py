class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (i, j) -> (n - j - 1, i)

        # MAGIC SOL (idk how i did this one)

        # n = len(matrix)
        # for i in range(n // 2):
        #     for j in range(n // 2, n):
        #         matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

        # INTUITIVE SOL

        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]