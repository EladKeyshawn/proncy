import dicts
import utils



reg_letters_dic = dicts.reg_letters_dic
dicts_list = dicts.dicts
c_cond = dicts.c_conditions
e_cond = dicts.e_conditions
spec_vowls = dicts.specialVowls
init_lett_len1 = dicts.initial_letters_len1
init_lett_len2 = dicts.initial_letters_len2


# find matches for subset withing different dictionaries
def find_matches(subset, start_index):
    # sort cases by len of subset
    length = len(subset)
    # if length == 1:

    if start_index == 0:
        if length == 2:
            if subset in init_lett_len2:
                return init_lett_len2[subset]

    if length == 2:
        if subset in c_cond:
            return c_cond[subset]
        if subset in e_cond:
            return e_cond[subset]
        if subset in spec_vowls:
            return spec_vowls[subset]
        if subset[0] == subset[1] and subset[0] in reg_letters_dic:
            return reg_letters_dic[subset[0]]



    for dict in dicts_list:
        if(subset in dict):
            return dict[subset]

    # if len(subset) == 1:
    #     if subset in dicts.wordBeginPronun:
    #         return dicts.wordBeginPronun[subset]

    return 'none'


class WordAnalyzer:
    def __init__(self, input, len):
        self.input = input
        self.length = len


    def start_analyzing(self):
        print("Starting analysis...")
        word = self.input # initial word string
        result = ""
        start_index_for_subset = 0 # marking the first letter from which we generate subsets

        while(start_index_for_subset < len(word)):
            curr_subsets = utils.get_string_subsets(word[start_index_for_subset:]) # passing our subsets gen the word from start index
            for subset in reversed(curr_subsets): # traversing subsets from the longest to catch larger conditions
                matched_val = find_matches(subset, start_index_for_subset)
                if matched_val != "none":
                    result += matched_val
                    start_index_for_subset += len(subset) # moving subset_index by the num of letters mapped
                    break

        print result




word = WordAnalyzer('subliminal', 6)
word.start_analyzing()












'''
     *** Comments and new cases for improving algorithm ***
     - IMPORTANT: need to check for letters like 'e' as first letters
     - check 'u' letter between two reg letters

'''
