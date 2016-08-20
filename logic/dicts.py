# -*- coding: UTF-8 -*-


 # Useful english letters to hebrew dicts



 # Bold letter dict from en to he
enLetterToHeb = {'a': 'א', 'b': 'ב', 'd': 'ד', 'f':'פ','h': "ה",  'j' : "ג'", 'k' : 'ק' , 'l': "ל", 'm': "מ", 'n': "נ",
                 'o':"ו", 'p': "פ" , 'q': "ק" , 'r': "ר" , 's': "ס", 't': 'ת',
                 'u': "ו", 'v' : "ב", 'w': "וו", 'x': 'קס', 'z': "ז"}



# Useful combinations
commonSyllablesDict = {'ea':"י", 'igh': "יי", 'th':"ת'" , 'ch': "צ'", 'ee': "י"}


# Vowels
vowelsDict = {'a': "", 'e': "", 'i': "י", 'o': "ו", 'u': "ו"}


# dict of consecutive vowels with removed middle reg letter

remMidVowels = {'ea': "יי"}


def testDicOutput():
    print commonSyllablesDict['th'] + commonSyllablesDict['ea'] + commonSyllablesDict['igh']


testDicOutput()