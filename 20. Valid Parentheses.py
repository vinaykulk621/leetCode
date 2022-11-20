class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if not stack:
                stack.append(i)
            elif stack[-1]=='(' and i==')':
                stack.pop()
            elif stack[-1]=='[' and i==']':
                stack.pop()
            elif stack[-1]=='{' and i=='}':
                stack.pop()
            elif (stack[-1]=='(' and i==']') or (stack[-1]=='(' and i=='}') or (stack[-1]=='[' and i==')') or (stack[-1]=='[' and i=='}') or (stack[-1]=='{' and i==')') or (stack[-1]=='{' and i==']'):
                return False
            else:
                stack.append(i)
        if stack:
            return False
        return True
