spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(listVar):
    if len(listVar) == 0: #condition for empty list
        return 'There are no items in the list.'

    elif len(listVar) == 1: #condition for a list with one item
        return str(listVar[0]) + '.' #or f'{listVar[0]}.'

    elif len(listVar) == 2: #condition for a list with two items
        return str(listVar[0]) + ' and ' + str(listVar[1]) + '.'
        #or f'{listVar[0]} and {listVar[1]}.'

    elif len(listVar) >= 3: #condition for a list with more than three items
        output = ''
        for i in range(len(listVar[:-1])):
            output += str(listVar[i]) + ', '

        output += 'and ' + str(listVar[-1])
        return output

print(commaCode(spam))
