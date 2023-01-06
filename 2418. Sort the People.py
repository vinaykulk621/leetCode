class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp=[(height,name) for height,name in zip(heights,names)]
        temp.sort(reverse=True)
        return [ch[1] for ch in temp]
