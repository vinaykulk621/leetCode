class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for val in nums1:
            if val in nums2:
                ans.append(val)
                nums2.remove(val)
        return ans
