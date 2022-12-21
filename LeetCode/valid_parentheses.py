# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {')': '(', '}': '{', ']': '['}
        stack_item = []

        for c in s:
            if len(stack_item) == 0:
                if c == ')' or c == '}' or c == ']':
                    return False
            if c in my_dict:
                if my_dict[c] != stack_item[-1]:
                    return False
                else:
                    stack_item.pop(-1)
                    continue
            stack_item.append(c)
        
        return len(stack_item) == 0

sol = Solution()
print(sol.isValid("(){}[]"))