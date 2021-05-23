langDict = {'python':'Guido Van Rossum',
      'java':'James Gosling',
      'c++':'Bjarne Stroustrup',
      'php':'Rasmus Lerdorf'}

while True:
    try:
        language = input('Enter the name of language whom you inventor you want to know [python, java, c++, php]: ').lower()
        print(f'{langDict[language]} invented {language}')
    except:
        print('The name you entered is not recognizable')
        pass
