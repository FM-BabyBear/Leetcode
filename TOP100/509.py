# unDown
class Solution:
    # Time: O(n)
    # Space: O(n)
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        arr = [0, 1]

        num = 2
        while num <= n:
            sum = arr[num - 1] + arr[num - 2]
            arr.append(sum)
            num += 1

        return arr[-1]
