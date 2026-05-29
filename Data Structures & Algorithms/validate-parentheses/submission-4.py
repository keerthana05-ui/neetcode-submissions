class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        stack = []
        append = stack.append
        pop = stack.pop
        
        for char in s:
            if char == '(':
                append(')')
            elif char == '[':
                append(']')
            elif char == '{':
                append('}')
            elif not stack or pop() != char:
                return False
                
        return not stack