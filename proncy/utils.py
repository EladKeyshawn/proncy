
# @params:
#  str - string to perform subsets breakdown
#  n (optional) - nth order to break


def get_string_subsets(str):
    subsets = []
    for index in range(len(str)):
        if(index == 0):
            subsets.append(str[index])
        else:
            subsets.append(subsets[index-1] + str[index])


    return subsets


