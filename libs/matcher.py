import dicts

reg_letters_dic = dicts.reg_letters_dic
dicts_list = dicts.dicts
c_cond = dicts.c_conditions
e_cond = dicts.e_conditions
g_cond = dicts.g_conditions
spec_vowls = dicts.special_vowls_len2
init_lett_len1 = dicts.initial_letters_len1
init_lett_len2 = dicts.initial_letters_len2
end_lett_len1 = dicts.end_letters_len1

# find matches for subset withing different dictionaries
def find_matches(subset, start_index, word):
    # sort cases by len of subset
    length = len(subset)
    # if length == 1:


    if start_index == 0:
        if length == 2:
            if subset in init_lett_len2:
                return init_lett_len2[subset]

    if start_index == len(word):
        if subset in end_lett_len1:
            return end_lett_len1[subset]

    if length == 2:
        if subset in c_cond:
            return c_cond[subset]
        if subset in e_cond:
            return e_cond[subset]
        if subset in g_cond:
            return g_cond[subset]
        if subset in spec_vowls:
            return spec_vowls[subset]
        if subset[0] == subset[1] and subset[0] in reg_letters_dic:
            return reg_letters_dic[subset[0]]

    if length == 3:
        if subset in g_cond:
            return g_cond[subset]
    # last resort
    for dict in dicts_list:
        if(subset in dict):
            return dict[subset]

    return 'none'


