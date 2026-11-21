class Solution:
    # Time: O(n) n: row * col of the image
    # Space: O(n)
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        row = len(image)
        col = len(image[0])
        originColor = image[sr][sc]

        def dfs(r: int, c: int):
            if image[r][c] == originColor:
                image[r][c] = color
                # left
                if c - 1 >= 0:
                    dfs(r, c - 1)

                # right
                if c + 1 < col:
                    dfs(r, c + 1)

                # top
                if r - 1 >= 0:
                    dfs(r - 1, c)

                # bottom
                if r + 1 < row:
                    dfs(r + 1, c)

        if image[sr][sc] != color:
            dfs(sr, sc)

        return image
