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

    # recursive
    # Time: O(2^n)
    # Space: O(n)
    def fib2(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib2(n - 1) + self.fib2(n - 2)

    # Time: O(n)
    # Space: O(n)
    def fib3(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        dict = {0: 0, 1: 1}

        dict[n] = self.fib3(n - 1) + self.fib3(n - 2)

        return dict[n]

    # Time: O(n)
    # Space: O(1)
    def fib4(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        num = 2
        sum = 0
        prev1 = 0
        prev2 = 1

        while num <= n:
            sum = prev1 + prev2
            prev1 = prev2
            prev2 = sum
            num += 1

        return sum
