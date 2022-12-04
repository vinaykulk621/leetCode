class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence=sentence.split()
        print(sentence)
        for i in range(len(sentence)):
            word=sentence[i]
            try:
                nextWord=sentence[i+1]
            except:
                nextWord=sentence[0]
            if word[-1]!=nextWord[0]:
                return False
        return True
