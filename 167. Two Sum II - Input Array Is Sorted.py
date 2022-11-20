class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right,answer=0,len(numbers)-1,[]
        while left<right:
            res=numbers[left]+numbers[right]
            if res==target:
                answer.append(left+1)
                answer.append(right+1)
                break
            elif res>target:
                right-=1
            elif res<target:
                left+=1
            else:
                left+=1
                right-=1
        return answer
