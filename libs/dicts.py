# -*- coding: UTF-8 -*-


# Dictionaries of English letters & syllables to Hebrew

basic_dicts = []



 # Bold letter dict from en to he
reg_letters_dic = {'a': 'א', 'b': 'ב', 'c': "ק",'d': 'ד', 'f':'פ','g' : "ג",'h': "ה",  'j' : "ג'", 'k':'ק' , 'l': "ל", 'm': "מ", 'n': "נ",
                 'o':"ו", 'p': "פ" , 'q': "ק" , 'r': "ר" , 's': "ס", 't': 'ת',
                 'u': "ו", 'v' : "ו", 'w': "וו", 'x': 'קס', 'z': "ז"}

# if regular letter repeats itself the output's the same as one

# Useful combinations
# commonSyllablesDict = {'ea':"י", 'igh': "יי" , 'ee': "י"}


# Vowels
vowels = {'a': "", 'e': "", 'i': "י", 'o': "ו", 'u': "ו"}


# special chars combinations
special_vowls_len2 = {'sh' : 'ש', 'ch' : 'צ׳', 'ph': "פ", 'th': "ת׳", 'ss' : "ש"}


# dict of consecutive vowels with removed middle reg letter
# meaning words like 'Rate' if reg letter trapped with a & e -> ea + reg letter -> 'ייט'


# special pronunciation at word's beginning
initial_letters_len1 = {'i': "אי", "k": "", 'a': "א", 'e': "א", 'y' : "י", 'u' : "א"}

initial_letters_len2 = {'ig': "איג", 'ee' : "אי" }


end_letters_len1 = {'e': ""}



# special individual letters with different sound under curtain circumstances
c_conditions = {'ce':"ס", 'ci': "סי", 'cy': "סיי"}

g_conditions = {'ge': "ג׳י" ,'gi': "ג׳י" ,'gy' : "ג׳יי",'get' : "גט"}

e_conditions = {'ee': 'י', 'ea' : 'י' }


# common short words for quick turn up
common_words = {'i' : "איי", 'we' : "ווי", 'she' : 'שי' , 'all': 'אול', 'the': 'ת׳י', 'or' : 'אור'}

seperate_dicts = []
seperate_dicts.append(common_words)

basic_dicts.append(reg_letters_dic)
basic_dicts.append(vowels)
basic_dicts.append(special_vowls_len2)
basic_dicts.append(c_conditions)
basic_dicts.append(e_conditions)
basic_dicts.append(g_conditions)
basic_dicts.append(initial_letters_len1)
basic_dicts.append(initial_letters_len2)
basic_dicts.append(end_letters_len1)
