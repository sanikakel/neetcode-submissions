class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for i in s:
            if i not in pmap:
                if len(stack) < 1:
                    return False
                x = stack.pop()
                if pmap[x] != i:
                    return False
            else: 
                stack.append(i)
        return len(stack) == 0