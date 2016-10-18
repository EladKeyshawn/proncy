# -*- coding: UTF-8 -*-


# Useful english letters to hebrew dicts



 # Bold letter dict from en to he
enLetterToHeb = {'a': 'א', 'b': 'ב', 'd': 'ד', 'f':'פ','h': "ה",  'j' : "ג'", 'k':'ק' , 'l': "ל", 'm': "מ", 'n': "נ",
                 'o':"ו", 'p': "פ" , 'q': "ק" , 'r': "ר" , 's': "ס", 't': 'ת',
                 'u': "ו", 'v' : "ב", 'w': "וו", 'x': 'קס', 'z': "ז"}

# if regular letter repeats itself the output's the same as one

# Useful combinations
commonSyllablesDict = {'ea':"י", 'igh': "יי", 'th':"ת'" , 'ch': "צ'", 'ee': "י"}


# Vowels
vowelsDict = {'a': "", 'e': "", 'i': "י", 'o': "ו", 'u': "ו"}


# special chars combinations

specialVowls = {'sh' : 'ש', 'ch' : 'צ׳'}

# dict of consecutive vowels with removed middle reg letter
# meaning words like 'Rate' if reg letter trapped with a & e -> ea + reg letter -> 'ייט'
remMidVowels = {'ea': "יי"}


# special pronunciation at word's beginning

wordBeginPronun = {'i': "איי", "k":"", 'a': "א", 'e': "א", 'ig': "איג",}

def testDicOutput():
    print specialVowls['ch']


testDicOutput()