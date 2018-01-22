'''
if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase
letter and one lowercase letter in it. The password contains only ASCII latin letters or digits
'''

def checkio(data):
    a = set()
    b = {'len', 'dig', 'lower', 'supper'}
    if len(data) > 10:
        a.add('len')
    for i in data:
        if i.isdigit():
            a.add('dig')
        elif i.islower():
            a.add('lower')
        elif i.isupper():
            a.add('supper')
    if a == b:
        return True
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

