class Solution:
    def longestValidParentheses(self, s: str) -> int:
        counter,stack=0,[-1]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    counter=max(counter,i-stack[-1])
        return counter
