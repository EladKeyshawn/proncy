import dicts


normLetter = dicts.enLetterToHeb
remMidVowels = dicts.remMidVowels

def isRegLetter(letter):
    return letter in normLetter


def isVowelLetter(currLetter):
    return currLetter in dicts.vowelsDict


class WordAnalyzer:
    def __init__(self, givenInput, len):
        self.input = givenInput
        self.length = len


    def startAnalyzing(self):
        print("Starting analysis...")
        engString = self.input
        for index in range(self.length - 1):
           currLetter = engString[index]
           if isRegLetter(engString[index]):
               print normLetter[engString[index]],
           elif index + 1 < self.length and index > 0:
               befAndAf = engString[index-1] + engString[index+1]
               midLetter = engString[index]
               if isRegLetter(engString[index]) and ( befAndAf in remMidVowels):
                   print(remMidVowels[befAndAf] , midLetter ,)

           elif isVowelLetter(currLetter):
               print(dicts.vowelsDict[currLetter],)





word = WordAnalyzer("idle", 7)
word.startAnalyzing()

