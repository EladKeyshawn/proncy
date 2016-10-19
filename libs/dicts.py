# -*- coding: UTF-8 -*-


# Dictionaries of English letters & syllables to Hebrew

dicts = []



 # Bold letter dict from en to he
reg_letters_dic = {'a': 'א', 'b': 'ב', 'c': "ק",'d': 'ד', 'f':'פ','h': "ה",  'j' : "ג'", 'k':'ק' , 'l': "ל", 'm': "מ", 'n': "נ",
                 'o':"ו", 'p': "פ" , 'q': "ק" , 'r': "ר" , 's': "ס", 't': 'ת',
                 'u': "ו", 'v' : "ו", 'w': "וו", 'x': 'קס', 'z': "ז"}

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
initial_letters_len1 = {'i': "איי", "k": "", 'a': "א", 'e': "א", 'y' : 'י'}

initial_letters_len2 = {'ig': "איג", 'ee' : "אי"  }




# special individual letters with different sound under curtain circumstances
c_conditions = {'ce':"ס", 'ci': "סי", 'cy': "סיי"}

g_conditions = {}

e_conditions = {'ee': 'י', }



dicts.append(reg_letters_dic)
dicts.append(commonSyllablesDict)
dicts.append(vowelsDict)
dicts.append(specialVowls)
dicts.append(c_conditions)
dicts.append(e_conditions)
dicts.append(initial_letters_len1)
dicts.append(initial_letters_len2)

# def testDicOutput():
#     print specialVowls['ch']
#
#
# testDicOutput()