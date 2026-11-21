class Solution:
    # Time: O(n) n: length of operaions
    # Space: O(n)
    def calPoints(self, operations: list[str]) -> int:
        list = []

        for operation in operations:
            if operation == "C":
                list.pop()
            elif operation == "D":
                list.append(2 * list[-1])
            elif operation == "+":
                list.append(list[-2] + list[-1])
            else:
                list.append(int(operation))

        return sum(list)
