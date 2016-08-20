# -*- coding: UTF-8 -*-


 # Useful english letters to hebrew dicts

 # Bold letter dict from en to he
enLetterToHeb = {'a': 'א', 'b': 'ב', 'd': 'ד', 'f':'פ', 'j' : "ג'", 'k' : 'ק' , 'l': "ל", 'm': "מ", 'n': "נ",
                 'o':"ו", 'p': "פ" , 'q': "ק" , 'r': "ר" , 's': "ס", 't': 'ת', 'u': "ו", 'v' : "ו", 'w': "וו", 'x': 'קס', 'z': "ז"}


# Useful combinations

commonSyllablesDict = {'ea':"י", 'igh': "יי", 'th':"ת'" }

def testDicOutput():
    print commonSyllablesDict['th'] + commonSyllablesDict['ea'] + commonSyllablesDict['igh']


testDicOutput()