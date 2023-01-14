enter = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
rows = [[enter[0], enter[1], enter[2]],
        [enter[3], enter[4], enter[5]],
        [enter[6], enter[7], enter[8]],
        [enter[0], enter[3], enter[6]],
        [enter[1], enter[4], enter[7]],
        [enter[2], enter[5], enter[8]],
        [enter[0], enter[4], enter[8]],
        [enter[2], enter[4], enter[6]]]


def print_net():
    print(f'''---------
| {rows[0][0]} {rows[0][1]} {rows[0][2]} |
| {rows[1][0]} {rows[1][1]} {rows[1][2]} |
| {rows[2][0]} {rows[2][1]} {rows[2][2]} |
---------''')


print_net()
i = 0
while i < 9:
    coordinates = ''
    while True:
        coordinates = input()
        try:
            coordinates = [int(coordinates[0]), int(coordinates[2])]
        except TypeError:
            print('You should enter numbers!')
            continue
        else:
            if coordinates[0] < 1 or coordinates[0] > 3 or \
                    coordinates[1] < 1 or coordinates[1] > 3:
                print('Coordinates should be from 1 to 3!')
                continue
            elif rows[coordinates[0] - 1][coordinates[1] - 1] != ' ':
                print('This cell is occupied! Choose another one!')
                continue
        break

    if i % 2:
        rows[coordinates[0] - 1][coordinates[1] - 1] = 'X'
    else:
        rows[coordinates[0] - 1][coordinates[1] - 1] = 'O'
    print_net()

    if ['X', 'X', 'X'] in rows and ['O', 'O', 'O'] in rows or abs(enter.count("X") - enter.count("O")) >= 2:
        print('Impossible')
    elif ['X', 'X', 'X'] not in rows and ['O', 'O', 'O'] not in rows:
        if '_' in enter:
            print('Game not finished')
        else:
            print('Draw')
    elif ['X', 'X', 'X'] in rows:
        print('X wins')
        break
    elif ['O', 'O', 'O'] in rows:
        print('O wins')
        break
