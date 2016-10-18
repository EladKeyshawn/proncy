from libs import dicts

reg_letters_dic = dicts.reg_letters_dic
remMidVowels = dicts.remMidVowels

def isRegLetter(letter):
    return letter in reg_letters_dic


def isVowelLetter(currLetter):
    return currLetter in dicts.vowelsDict


def checkBeginPronun(currLetter):
    return currLetter in dicts.wordBeginPronun



class WordAnalyzer:
    def __init__(self, givenInput, len):
        self.input = givenInput
        self.length = len


    def startAnalyzing(self):
        print("Starting analysis...")
        word = self.input # initial string
        index = 0
        while index < len(word):
           currLetter = word[index]
           if checkBeginPronun(currLetter):
               print dicts.wordBeginPronun[currLetter] ,

           elif isRegLetter(word[index]):
               print reg_letters_dic[word[index]],

           elif (index + 1 < self.length and index > 0):
               befAndAf = word[index-1] + word[index+1]
               midLetter = word[index]

               if isRegLetter(midLetter) and ( befAndAf in remMidVowels):
                   print(remMidVowels[befAndAf] , reg_letters_dic[midLetter] ,)

           elif isVowelLetter(currLetter):
               print dicts.vowelsDict[currLetter],

           index += 1



word = WordAnalyzer("idle", 6)
word.startAnalyzing()












'''
     *** Comments and new cases for improving algorithm ***
     - check 'u' letter between two reg letters

'''
