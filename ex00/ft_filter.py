def ft_filter(function_to_apply, list_of_inputs):
    res = []
    if function_to_apply is None:
        for elem in list_of_inputs:
            if elem:
                res.append(elem)
    else:
        for elem in list_of_inputs:
            if function_to_apply(elem):
                res.append(elem)
    return res


# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o', False, True]


# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    else:
        return False


filteredVowels = ft_filter(filterVowels, alphabets)
print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)
