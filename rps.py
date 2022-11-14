import random
import sys
import time
score = [0, 0]
print('Welcome to Rock, Paper, Scissors. You may exit anytime using \'gg\'. Have fun!')
choice_dict = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
cheat_list = ['Hold on one sec', 'Don\'t mind me. I\'m just gonna', 'Hey, look behind you for a minute',
              'It says gullible on the ceiling']
cheat_lines = ['You saw nothing 0_0', 'I didn\'t do anything', 'Nobody will believe you :)', 'Whaaaat?',
               'Weird, I\'m not sure what happened there', 'Don\'t mind that']

def rps(user, choices):
    cpu = random.choice(choices)
    cheat = random.randint(0, 10)
    if score[0] == 2 and cheat >= 5:
        print(random.choice(cheat_list), end='')
        for x in range(0, 5):
            print('.', end='')
            time.sleep(1.5)
        print('.')
        time.sleep(1.5)
        print('user_score = user_score - 1')
        score[0] = score[0] - 1
        time.sleep(1.5)
        print(random.choice(cheat_lines))
        time.sleep(1.5)
    elif user == 'r' and cpu == 'p':
        print('CPU WINS! Your rock does not beat CPU\'s paper')
        score[1] += 1
    elif user == 'p' and cpu == 's':
        print('CPU WINS! Your paper does not beat CPU\'s scissors')
        score[1] += 1
    elif user == 's' and cpu == 'r':
        print('CPU WINS! Your scissors do not beat CPU\'s rock')
        score[1] += 1
    elif user == cpu:
        print(f'TIE! Your {choice_dict[user]} and CPU\'s {choice_dict[cpu]} tie')
    else:
        print(f'USER WINS! CPU\'s {choice_dict[cpu]} can\'t compete with your {choice_dict[user]}')
        score[0] += 1
    print(f'Score: {score[0]}:{score[1]}')
    main()

def main():
    choices = ['r', 'p', 's']
    if score[0] == 3:
        print(f'You Win! {score[0]} to {score[1]} :)')
        sys.exit()
    elif score[1] == 3:
        print(f'You Lose! {score[0]} to {score[1]} :(')
        sys.exit()
    while True:
        user = input('Rock(\'r\'), Paper(\'p\'), or scissors(\'s\')?: ')
        if user.lower() == 'gg':
            print('GG!')
            sys.exit()
        elif user.lower() in choices:
            break
    rps(user.lower(), choices)

if __name__ == '__main__':
    main()
