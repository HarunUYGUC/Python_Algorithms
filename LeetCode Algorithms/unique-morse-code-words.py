""" https://leetcode.com/problems/unique-morse-code-words/ """

class Solution:
    def uniqueMorseRepresentations(self, words):
        morseCodeAlphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
                             "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        englishAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                           "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        morseCodeWords = []

        for word in words:
            morseCodeWord = ""

            for c in word:
                engAlphIndex = englishAlphabet.index(c)
                morseCodeChar = morseCodeAlphabet[engAlphIndex]
                morseCodeWord += morseCodeChar
            
            morseCodeWords.append(morseCodeWord)
        
        differentTransformations = 0

        while (len(morseCodeWords) != 0):
            wordToBeDeleted = morseCodeWords[0]
            count = morseCodeWords.count(wordToBeDeleted)

            while (count > 0):
                morseCodeWords.remove(wordToBeDeleted)
                count -= 1

            differentTransformations += 1

        return differentTransformations

print(Solution().uniqueMorseRepresentations(["qqbp","gmyhg","bduo","drvmt","nsszh","bhzh","nglsm","tplsm","nzthw",
                                             "yfsw","kxhw","xeujq","navaota","jhbek","wbahk","wbahk","jhbek","yuvg","yuvg","yusmn"]))
