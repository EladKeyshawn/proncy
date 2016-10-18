import dicts
import utils



reg_letters_dic = dicts.reg_letters_dic
dicts_list = dicts.dicts

# find matches for subset withing different dictionaries
def find_matches(subset):
    for dict in dicts_list:
        if(subset in dict):
            return dict[subset]

    return 'none'


class WordAnalyzer:
    def __init__(self, givenInput, len):
        self.input = givenInput
        self.length = len


    def start_analyzing(self):
        print("Starting analysis...")
        word = self.input # initial word string
        result = ""
        start_index_for_subset = 0 # marking the first letter from which we generate subsets

        while(start_index_for_subset < len(word)):
            curr_subsets = utils.get_string_subsets(word[start_index_for_subset:]) # passing our subsets gen the word from start index
            for subset in reversed(curr_subsets): # traversing subsets from the longest to catch larger conditions
                matched_val = find_matches(subset)
                if matched_val != "none":
                    result += matched_val
                    start_index_for_subset += len(subset)
                    break

        print result





word = WordAnalyzer("insist", 6)
word.start_analyzing()












'''
     *** Comments and new cases for improving algorithm ***
     - IMPORTANT: need to check for letters like 'e' as first letters
     - check 'u' letter between two reg letters

'''
