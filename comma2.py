#This program will print any number of list you enter
#Each list separated by comma,and 'and ' is added before the last element.

def comma(list):
    result = ''
    length = len(list)
    if length == 0:
        result = 'You gave me nothing.'
    elif length == 1:
        result = list[0]
    else:
        for i in range(length - 1):
            result += list[i] + ', '
        result += 'and ' + list[-1]
    return result

spam = []

while True:
    print('Please type list' + str(len(spam) + 1) + '(You have done, press only Enter key.)')
    l = input()
    if l == '':
        break
    spam = spam + [l]
    
print("'"  + comma(spam) + "'")
