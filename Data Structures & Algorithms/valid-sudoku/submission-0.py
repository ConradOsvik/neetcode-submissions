class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [{} for _ in range(len(board))]
        squares = [[{} for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            row = board[i]
            nums = set()
            for j in range(len(board[0])):
                num = row[j]

                if num == ".":
                    continue

                if num in nums:
                    return False
                nums.add(num)

                if num in columns[j]:
                    return False
                columns[j][num] = True

                if num in squares[i // 3][j // 3]:
                    return False
                squares[i // 3][j // 3][num] = True

        return True