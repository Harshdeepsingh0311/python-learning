# Exercise 7
# Healthy Programmer

# 9:00 to 5:00

# Water - 3.5 litres - water.mp3 - Drank - log - Every 40 min
# Eye - 30 minute - eye.mp3 - EyDone - log -
# Physical Activity - 45 minute - physical.mp3 - ExDone - log

# Rules - Use pygame

from pygame import mixer
from datetime import datetime
from time import time

water_time = 40*60
eyes_time = 10
exercise_time = 45*60


def musicloop(file, stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        a = a.lower()

        if a == stop:
            mixer.music.stop()
            break

def log_now(msg):

    with open('mylogs.txt', 'a') as f:
        f.write(f'{msg} {datetime.now()}\n')

if __name__ == '__main__':
    # musicloop('water.mp3','stop')
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    while True:
        if time() - init_water > water_time:
            print('Its water drinking time!!\nEnter \'drank\' to stop the alarm')
            musicloop('water.mp4', 'drank')
            init_water = time()
            log_now('Drank water at')

        elif time() - init_eyes > eyes_time:
            print('Its time for eyes exercise!!\nEnter \'Eydone\' to stop the alarm')
            musicloop('eye.mp4', 'eydone')
            init_eyes = time()
            log_now('Did eyes exercise at')

        elif time() - init_exercise > exercise_time:
            print('Its time to do some physical activities!!\nEnter \'Exdone\' to stop the alarm')
            musicloop('exercise.mp4', 'exdone')
            init_eyes = time()
            log_now('Did some physical activities at')

        else:
            pass
