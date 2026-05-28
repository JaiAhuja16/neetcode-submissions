class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in s:
                    return False
                else:
                    s.add(num)
        for j in range(9):
            s = set()
            for i in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in s:
                    return False
                else:
                    s.add(num)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i + k][j + l]
                        if num == '.':
                            continue
                        if num in s:
                            return False
                        else:
                            s.add(num)
        return True