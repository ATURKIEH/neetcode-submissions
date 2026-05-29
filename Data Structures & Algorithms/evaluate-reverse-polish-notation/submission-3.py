from functools import reduce
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        seen_list = []
        operations = ['+', '-', '*', '/']

        for element in tokens:
            if element in operations:
                x = seen_list.pop()
                y = seen_list.pop()
                if element == '+':
                    sum = y+x
                    seen_list.append(sum)

                elif element == '-':
                    sum = y - x
                    seen_list.append(sum)

                elif element == '*':
                    sum = y * x
                    seen_list.append(sum)

                elif element == '/':
                    sum = y / x
                    seen_list.append(int(sum))

                else:
                    return
            else:
                seen_list.append(int(element))

        return seen_list[0]

        