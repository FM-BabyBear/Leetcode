# use stack


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in s:

            if char in pairs:
                top = stack.pop()
                if top != pairs[char]:
                    return False

            else:
                stack.append(char)

        print("stack ", stack)

        if len(stack) > 0:
            return False

        return True


def main() -> None:
    solution = Solution()
    res = solution.isValid("()")
    print("res ", res)


main()
