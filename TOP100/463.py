class Solution:
    def onelandPerimeter(self, land: tuple[int, int], grid: list[list[int]]) -> int:
        x, y = land
        row = len(grid)
        column = len(grid[0])
        landNum = 0

        # left
        if y > 0 and grid[x][y - 1] == 1:
            landNum += 1
        # right
        if y < column - 1 and grid[x][y + 1] == 1:
            landNum += 1
        # top
        if x > 0 and grid[x - 1][y] == 1:
            landNum += 1
        # down
        if x < row - 1 and grid[x + 1][y] == 1:
            landNum += 1

        return 4 - landNum

    # Time: O(MN) M: Rows; N: Columns
    # Space: O(1)
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        total = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] != 0:
                    total += self.onelandPerimeter((i, j), grid)

        return total

    # Time: O(MN) M: Rows; N: Columns
    # Space: O(1)
    def islandPerimeter2(self, grid: list[list[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        total = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    total += 4
                    # top
                    if i > 0 and grid[i - 1][j] == 1:
                        total -= 2
                    # left
                    if j > 0 and grid[i][j - 1] == 1:
                        total -= 2

        return total
