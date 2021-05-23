# Faulty Calculator
# 45*3=555, 56+9=77, 56/6=4

while True:
    a = input('Enter the first number: ')
    c = input('Enter the Operator: ')
    b = input('Enter the second number: ')

    if '45' in a and '3' in b and '*' in c:
        print('The answer is 555')

    elif '56' in a and '9' in b and '+' in c:
        print('The answer is 77')

    elif '56' in a and '6' in b and '/' in c:
        print('The answer is 4')

    else:
        if '+' in c:
            print('The answer is', int(a)+int(b))
        elif '-' in c:
            print('The answer is', int(a)-int(b))
        elif '*' in c:
            print('The answer is', int(a)*int(b))
        elif '/' in c:
            print('The answer is', int(a)/int(b))
        else:
            print('Invalid operator or operand...')
