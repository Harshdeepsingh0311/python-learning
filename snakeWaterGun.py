from random import choice
from time import sleep

game_char = ['Snake', 'Water', 'Gun']
player = 0
computer = 0
win = f'Computer: {computer} player: {player}'
delay_time = 1


while True:

    try:
        if computer == 2 or player == 2:
            print('Player wins!!') if player > computer else print('Computer wins!!')
            exit()

        else:
            chosen_char = choice(game_char)
            print('\nSnake, Water, Gun')
            sleep(delay_time)
            chosen_player = input('Enter your character: ')
            chosen_player = chosen_player.capitalize()
            sleep(delay_time)
            print(f'Computer chose {chosen_char}')
            sleep(delay_time)
            print(f'You chose {chosen_player}')
            sleep(delay_time)

            if chosen_char == chosen_player:
                print('Tie, Try again...')
                sleep(delay_time)
                print('Snake Water Gun')
                print(f'Computer: {computer} player: {player}')

            elif chosen_char == 'Snake':
                if chosen_player == 'Water':
                    print('Computer Wins!!, Snake drank the water.')
                    computer += 1
                    sleep(delay_time)
                    print(f'Computer: {computer} player: {player}')

                elif chosen_player == 'Gun':
                    print('Player Wins!!, Gun shot the snake.')
                    player += 1
                    sleep(delay_time)
                    print(f'Computer: {computer} player: {player}')

                else:
                    print('Enter a valid character')

            elif chosen_char == 'Water':
                if chosen_player == 'Snake':
                    print('Player Wins!!, Snake drank the water.')
                    player += 1
                    sleep(delay_time)
                    print(f'Computer: {computer} player: {player}')

                elif chosen_player == 'Gun':
                    print('Computer Wins!!, Gun sank in the water.')
                    computer += 1
                    sleep(delay_time)
                    print(f'Computer: {computer} player: {player}')

                else:
                    print('Enter a valid character')

            elif chosen_char == 'Gun':
                if chosen_player == 'Snake':
                    print('Computer Wins!!, Gun shot the snake.')
                    computer += 1
                    sleep(delay_time)
                    print(f'Computer: {computer} player: {player}')

                elif chosen_player == 'Water':
                    print('Player Wins!!, Gun sank in the water.')
                    player += 1
                    sleep(delay_time)
                    print(f'Computer: {computer} player: {player}')

                else:
                    print('Enter a valid character')

    except Exception as e:
        print(e)
