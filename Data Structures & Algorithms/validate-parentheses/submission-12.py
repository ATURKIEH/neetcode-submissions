class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       open_set = ['(', '{', '[']
       close_set = [')', '}', ']']
       match = {'(':')', '{' : '}', '[': ']'}

       for bracket in s:
            if bracket in open_set:
                stack.append(bracket)

            else:
                if not stack:
                    return False
                
                else:
                    bracket_popped = stack.pop()
                    if match[bracket_popped] != bracket:
                        return False

       if len(stack) == 0:
            return True
       else:
        return False


