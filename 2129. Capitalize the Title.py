class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title,ans=title.split(),[]
        for ch in title:
            if len(ch)<=2:
                ans.append(ch.lower())
            else:
                ans.append(ch.title())
        return " ".join(ans)
