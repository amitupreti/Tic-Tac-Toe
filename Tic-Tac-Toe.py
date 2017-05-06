# this is  tic tac toe a simple game yet popular game
#
print('---------------------------TIC TAC TOE-----------------------------\n')
print('\t\t\t___|__|___')
print('\t\t\t___|__|___')
print('\t\t\t   |  |   ')
print("please choose your symbol:\n1.Player1->X\n2.Player2->O\n>>")
print('\t\t\t_1|_2_|_3__')
print('\t\t\t_4|_5_|_6_')
print('\t\t\t 7| 8 | 9 ')
list_Pl1 = []
list_Pl2 = []
# we define empty list with 10 empty spaces
list = ['', '', '', '', '', '', '', '', '', '']

# this function will display the tic tac toe game display.here we have a list named list which stores the position input from players .
# i have created the list of 10 integers because i had some problems doing
# the program =>not important


def displayBoard(player, input):

    print('the input is', input)
    ''''''
    print("\t\t\t_", list[1], "_|_", list[2], "_|_", list[3], "_")
    print("\t\t\t_", list[4], "_|_", list[5], "_|_", list[6], "_")
    print("\t\t\t_", list[7], "_|_", list[8], "_|_", list[9], "_")

# here we check if the position entered by user is already taken or not.since we defined it as '' in  beginning
# we only need to check whether the list item is equal to ''  ,if not
# then the position is not free


def check_input(input_pl):
    if list[input_pl] == '':
        return True
    else:
        return False

# here we check winning condition for tic tac toe.we compaare with a value
# i.e. 'X' or 'O'


def winner(chk):
    return (list[1] == list[2] == list[3] == chk or
            list[4] == list[5] == list[6] == chk or
            list[7] == list[8] == list[9] == chk or
            list[1] == list[4] == list[7] == chk or
            list[2] == list[5] == list[8] == chk or
            list[3] == list[6] == list[9] == chk or
            list[1] == list[5] == list[9] == chk or
            list[7] == list[5] == list[3] == chk)


# main function

def play():
        # defining a variable list_input so that we can prevent player from
        # entering more than 9 values
    list_input = 1
    # this will be useful when player 2('O') enters the position already
    # occupied
    error_pl2 = 'off'
    while(list_input <= 9):  # ie loop runs for 9 values from players
        if(list_input % 2 != 0):  # since out list_input starts from 1 .so odd(1,3,5,7,9) means input from player 1("X") and even means player2("O")
            print('Player:X Enter your desired position')
            input_Pl1 = int(input(''))  # STORES INPUT from player 1
            # we are checking whether  the entered position is already taken
            # initially error_pl2 is off so 1st time if is satisfied
            if (check_input(input_Pl1)) and (error_pl2 == 'off'):
                # we are assigning the value 'X' ie username in the list,so
                # that it can  be displayed by Function displayBoard()
                list[input_Pl1] = "X"
                displayBoard('X', input_Pl1)
                # checking for winner .we supply value 'X' and check whether
                # "x" is winner or not
                if(winner('X')):
                    print("X is winner")
                    break
                    # we increase thelist_input variable so that we know that
                    # on position has been filled
                list_input += 1

            else:  # if position is already taken then  we continue the loop so again beginning from top
                print('the position is already taken.Please choose wisely player X\n`')
                continue
        else:
            # this part runs for evn vaue of list_input
            if(list_input != 9):
                print('Player:O Enter your desired position')

                input_Pl2 = int(input(''))
                if check_input(input_Pl2):

                    list[input_Pl2] = "O"
                    list_Pl2.append(input_Pl2)
                    if(winner("O")):
                        print("O is winner")
                        break
                    list_input += 1

                    displayBoard("O", input_Pl2)
                    error_pl2 = 'off'

                else:
                    print(
                        'the position is already taken .Please choose wisely player O \n')
                    # here we assign error_pl2 as on so that  for next
                    # iteration we can skip  asking input for player 1.
                    error_pl2 = 'on'
    repeat = input('do you want another game? y for yes and n for no?::')
    if(repeat == "y" or repeat == "Y"):
        play()
play()
