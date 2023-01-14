import random

msg_ = ["How many pencils would you like to use:",
        "The number of pencils should be numeric",
        "The number of pencils should be positive",
        "Who will be the first",
        "Choose between",
        "Possible values: '1', '2' or '3'",
        "Too many pencils were taken",
        " won!",
        "John's turn!",
        "Jack's turn:"]
player = 'John'
bot = 'Jack'
num_of_pencils = [1, 2, 3]
pencils = 0

print(msg_[0])

while True:
    try:
        pencils = int(input())
    except ValueError:
        print(msg_[1])
        continue
    if pencils < 0:
        print(msg_[1])
        continue
    if pencils == 0:
        print(msg_[2])
        continue
    break

print(f'{msg_[3]} ({player}, {bot}):')

while True:
    whose_turn = input()
    if whose_turn == player or whose_turn == bot:
        break
    print(f"{msg_[4]} '{player}' and '{bot}'")

print('|' * pencils)

while True:
    if whose_turn == player:
        print(msg_[8])
    elif whose_turn == bot:
        print(msg_[9])
    take_pencils = 0
    while True:
        if whose_turn == bot:
            if pencils % 4 == 0:
                take_pencils = 3
                print(take_pencils)
            elif pencils % 4 == 3:
                take_pencils = 2
                print(take_pencils)
            elif pencils % 4 == 2:
                take_pencils = 1
                print(take_pencils)
            elif pencils == 1:
                take_pencils = 1
                print(take_pencils)
            else:
                take_pencils = random.randint(1, 3)
                print(take_pencils)
        elif whose_turn == player:
            try:
                take_pencils = int(input())
            except ValueError:
                print(msg_[5])
                continue

        if take_pencils in num_of_pencils:
            if take_pencils > pencils:
                print(msg_[6])
                continue
            break
        print(msg_[5])

    pencils -= take_pencils
    if pencils != 0:
        print('|' * pencils)

    if whose_turn == player:
        whose_turn = bot
    elif whose_turn == bot:
        whose_turn = player
    if pencils == 0:
        print(f'{whose_turn}{msg_[7]}')
        break

