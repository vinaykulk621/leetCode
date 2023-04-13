class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]==popped[0]:
                stack.pop()
                popped.pop(0)
        return False if stack else True
