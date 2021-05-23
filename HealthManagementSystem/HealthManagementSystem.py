# Health Management System
# 3 Clients - Harsh, Hemang, Taran

# Total 6 files
# Write a function that when executed takes as input client name


import datetime

time = datetime.datetime.now()

f = open('Users.txt')
g = str(f.readlines())
usernames = g.replace('[', '')
usernames = usernames.replace(']', '')

f.close()

while True:
    f = open('Users.txt')
    g = str(f.readlines())
    usernames = g.replace('[', '')
    usernames = usernames.replace(']', '')

    f.close()
    try:
        name = input('Enter your nickname: ')
        name = name.lower()

        if name in usernames:
            query = int(input('Do you want to lock or retrieve\n1 to lock, 2 to retrieve: '))

            if query == 1:
                me_query = int(input('Do you want to lock your meal or exercise\n1 for meal, 2 for exercise: '))

                if me_query == 1:
                    data = input('Enter data: ')
                    try:
                        with open(f'{name}_meal.txt', 'x'):
                            with open(f'{name}_meal.txt', 'a') as f:
                                f.write(f'{time} : {data}')

                    except:
                        with open(f'{name}_meal.txt', 'a') as f:
                            f.write(f'{time} : {data}')

                elif me_query == 2:
                    data = input('Enter data: ')
                    with open(f'{name}_exercise.txt', 'x'):
                        with open(f'{name}_exercise.txt', 'a') as f:
                            f.write(f'{time} : {data}')

                else:
                    query = int(input('Please enter valid value\n1 to lock, 2 to retrieve: '))

                print('!!Data Added!!')

            elif query == 2:
                me_query = int(input('Do you want to retrieve your meal or exercise\n1 for meal, 2 for exercise: '))

                if me_query == 1:

                    with open(f'{name}_meal.txt', 'r') as f:
                        content = f.readlines()
                        print(content)

                elif me_query == 2:

                    with open(f'{name}_exercise.txt', 'r') as f:
                        content = f.readlines()
                        print(content)

                else:
                    query = int(input('Please enter valid value\n1 to lock, 2 to retrieve: '))

                print('!!Data Fetched!!')

            else:
                query = int(input('Please enter valid value\n1 to lock, 2 to retrieve: '))



        else:
            registration = input(
                'Sorry for inconvenience, you are not registered.'
                '\nDo you want to get registered? Enter y for yes and n for no: ')

            if registration == 'y':
                register_name = name.lower()
                file = open('Users.txt', 'a')
                file.write(f'\n{register_name}')
                file.close()

                with open(f'{register_name}_meal.txt', 'x'):
                    pass

                with open(f'{register_name}_exercise.txt', 'x'):
                    pass

                query = int(input('Do you want to lock or retrieve\n1 to lock, 2 to retrieve: '))

                if query == 1:
                    me_query = int(input('Do you want to lock your meal or exercise\n1 for meal, 2 for exercise: '))

                    if me_query == 1:
                        data = input('Enter data: ')
                        with open(f'{register_name}_meal.txt', 'a') as f:
                            f.write(f'{time} : {data}')

                    elif me_query == 2:
                        data = input('Enter data: ')
                        with open(f'{register_name}_exercise.txt', 'a') as f:
                            f.write(f'{time} : {data}')

                    else:
                        query = int(input('Please enter valid value\n1 to lock, 2 to retrieve: '))

                    print('!!Data Added!!')

                elif query == 2:
                    me_query = int(input('Do you want to retrieve your meal or exercise\n1 for meal, 2 for exercise: '))

                    if me_query == 1:
                        with open(f'{register_name}_meal.txt') as f:
                            content = f.readlines()
                            print(content)

                    elif me_query == 2:
                        with open(f'{register_name}_exercise.txt') as f:
                            content = f.readlines()
                            print(content)

                    else:
                        query = int(input('Please enter valid value\n1 to lock, 2 to retrieve: '))

                    print('!!Data Fetched!!')

                else:
                    query = int(input('Please enter valid value\n1 to lock, 2 to retrieve: '))

            else:
                continue

    except Exception as e:
        print(e)
