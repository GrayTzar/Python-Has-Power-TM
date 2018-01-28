import random


def field_gen(field):
    print("Here is your battlefield:\n")
    print('    A B C')  # 4 spaces for 3x3. I'll make it auto-generate based on field size later.
    print('  ~~~~~~~~~')  # 9 waves for 3x3. So, 3 + (2 * size)
    row_no = 0
    for row in field:
            row_no += 1
            print('%s ~ %s %s %s ~' % (row_no, row[0], row[1], row[2]))
    print('  ~~~~~~~~~')
    # I'll make this a function later to accommodate various sizes


# generate ships - second try
ships = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def gen_ships(number):
    for i in range(number):
        ship_row = random.randint(0, 2)
        ship_col = random.randint(0, 2)
        if ships[ship_row][ship_col] != 1:
            ships[ship_row][ship_col] = 1
        else:
            i += 1


print('Welcome to battleships!')  # greetings

name = input("What's your name? ")  # ask for name and welcome the user
print('Welcome, %s!' % name)

battlefield = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
# later I'll let the user define the size (3-7)

bfmap = {
    'A': 0,
    'B': 1,
    'C': 2,
    'a': 0,
    'b': 1,
    'c': 2
}


field_gen(battlefield)

ship_number = int(input('How many ships? (1-3)'))
gen_ships(ship_number)
# field_gen(ships) #  cheat mode


turns = int(input('How many turns? (1-4)'))
score = 0
for turn in range(turns):
    user_shot = input('Where are you shooting?\n')

    loc_y = bfmap[user_shot[0]]
    loc_x = int(user_shot[1]) - 1

    #  now we update the board
    if loc_y not in [0, 1, 2]:  # this list can later be a variable based on size
        print('Try again. Use the format: A1 or a1.')
    elif loc_x not in [0, 1, 2]:
        print('Try again. Use the format: A1 or a1.')
    else:
        if ships[loc_x][loc_y] == 1:
            battlefield[loc_x][loc_y] = 'X'
            ship_number -= 1
            print("It's a hit!")
            ships[loc_x][loc_y] = 100
            score = score + 1
        elif ships[loc_x][loc_y] == 0:
            battlefield[loc_x][loc_y] = '-'
            print("It's a miss!")
            ships[loc_x][loc_y] = 100
        elif ships[loc_x][loc_y] == 100:
            print("You already shot there!")
    field_gen(battlefield)
    if ship_number == 0:
        break


print('Thanks for playing! Your score is ' + str(score))
