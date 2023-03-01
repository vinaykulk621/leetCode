class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sortIt(nums):
            if len(nums)>1:
                left=nums[:len(nums)//2]
                right=nums[len(nums)//2:]

                sortIt(left)
                sortIt(right)

                i=j=k=0
                while i<len(left) and j<len(right):
                    if left[i]<right[j]:
                        nums[k]=left[i]
                        i+=1
                    else:
                        nums[k]=right[j]
                        j+=1
                    k+=1

                while i<len(left):
                    nums[k]=left[i]
                    k+=1
                    i+=1
                while j<len(right):
                    nums[k]=right[j]
                    k+=1
                    j+=1
            return nums
        return sortIt(nums)
