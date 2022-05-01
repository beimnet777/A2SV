class Solution:
    def countVowels(self, word: str) -> int:
        length=len(word)
        i=0
        total=0
        vowels=set(['a','e','i','o','u'])
        while i<length:
            if word[i] in vowels:
                total+=((length-i)*(i+1))
            i+=1
        return total
