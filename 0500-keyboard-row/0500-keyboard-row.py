class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        answer=[]
        row1=("qwertyuiop")
        row2=("asdfghjkl")
        row3=("zxcvbnm")
        for word in words:
            letters=set(word.lower())
            if letters.issubset(row1):
                answer.append(word)
            elif letters.issubset(row2):
                answer.append(word)
            elif letters.issubset(row3):
                answer.append(word)
        return answer

    