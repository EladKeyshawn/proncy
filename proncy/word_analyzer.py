import dicts
import utils
import matcher


# find matches for subset withing different dictionaries
# def find_matches(subset, start_index, word):
#     # sort cases by len of subset
#     length = len(subset)
#     # if length == 1:
#
#
#     if start_index == 0:
#         if length == 2:
#             if subset in init_lett_len2:
#                 return init_lett_len2[subset]
#
#     if start_index == len(word):
#         if subset in end_lett_len1:
#             return end_lett_len1[subset]
#
#     if length == 2:
#         if subset in c_cond:
#             return c_cond[subset]
#         if subset in e_cond:
#             return e_cond[subset]
#         if subset in g_cond:
#             return g_cond[subset]
#         if subset in spec_vowls:
#             return spec_vowls[subset]
#         if subset[0] == subset[1] and subset[0] in reg_letters_dic:
#             return reg_letters_dic[subset[0]]
#
#     if length == 3:
#         if subset in g_cond:
#             return g_cond[subset]
#     # last resort
#     for dict in dicts_list:
#         if(subset in dict):
#             return dict[subset]
#
#     return 'none'





def start_analyzing(input):
    print("Starting analysis...")
    word = input  # initial word string
    result = ""
    start_index_for_subset = 0  # marking the first letter from which we generate subsets

    while (start_index_for_subset < len(word)):
        curr_subsets = utils.get_string_subsets(
            word[start_index_for_subset:])  # passing our subsets gen the word from start index
        for subset in reversed(curr_subsets):  # traversing subsets from the longest to catch larger conditions
            matched_val = matcher.find_matches(subset, start_index_for_subset, word)
            if matched_val != "none":
                result += matched_val
                start_index_for_subset += len(subset)  # moving subset_index by the num of letters mapped
                break
            if len(subset) == 1:
                start_index_for_subset += 1
    print  result
    return result




start_analyzing("complicated")












'''
     *** Comments and new cases for improving algorithm ***
     - IMPORTANT: need to check for letters like 'e' as first letters
     - check 'u' letter between two reg letters
     - check 'ow'

'''
