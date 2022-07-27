
def listPrinter(list):
    for element in list:
        if element == list[-1]:
            print('and ' + str(element))
        else:
            print(str(element), end=', ')




spam = ['apples', 'bananas', 'tofu', 'cats']
spam1 = [1, 5, 2, 12, 95, -3]

listPrinter(spam)
listPrinter(spam1)
