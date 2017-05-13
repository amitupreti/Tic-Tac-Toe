import os
import time
def Display_board(board):
	'''Displayes the empty board before input and displayes values on board  after input by users'''
	os.system('clear') #for linux-->>> clears the screen
	#os.system('cls') for windows
	print("\t\t\t    |   | ")
	print("\t\t\t ",board[1],"|",board[2], "|",board[3],"")
	print("\t\t\t    |   | ")
	print("\t\t\t-------------")
	print("\t\t\t    |   | ")
	print("\t\t\t ",board[4],"|",board[5], "|",board[6],"")
	print("\t\t\t    |   | ")
	print("\t\t\t------------")
	print("\t\t\t    |   | ")
	print("\t\t\t ",board[7],"|",board[8], "|",board[9],"")
	print("\t\t\t    |   | ")


def inputPlayer():
	''' Asks names of two players and provides option to player 1 to choose X or O.player 2 gets the left value.
	Also prints  warning to users for wrong choices in X or O.outputs name in dictionary'''
	player=" "
	name1=input("please enter your name player1:")
	name2=input("please enter your name player2:")
	os.system("clear")
	while(player!="X" or player!="0"):
		player=input(">>>>>>>>"+name1+' Do You want to be player "X" or "O"??').upper()
		if player=="X":
			#dict={'Name':'Amit','Roll':60,'Phone':9843234311}	
			pl={"X":name1,"O":name2}
			return pl
		elif player == "O":
			pl={"O":name1,"X":name2}
			return pl
		else:
			errmsg=["Are You stupid?","Please chooose either X or O ","come on stop wasting time","Is it that Hard or is it you?"]
			import random
			val=random.randint(0, 3)
			print(errmsg[val])

			
		

def position_board(position,board,player):
	'''places  input value to a position in list .here name of list is board'''
	board[position] = player

def winner_check(board,player):
	'''checks for winner using the conditions of tic tac toe'''
	return (board[1] == board[2] == board[3] == player or
            board[4] == board[5] == board[6] == player or
            board[7] == board[8] == board[9] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[3] == board[6] == board[9] == player or
            board[1] == board[5] == board[9] == player or
            board[7] == board[5] == board[3] == player)


def go_first():
	'''uses a random function to choose which player goes first'''
	import random
	if random.randint(1, 2) == 1:
		return "X"
	else:
		return "O"

def position_Check(board,position):
	'''Boolean function:checks whether the position is availiable or not'''
	if board[position] == " ":
		return True
	else:
		return False

def board_Full(board,position_Check):
	'''Boolean function:checks if the board is full'''
	for num in range(1,10):
		if position_Check(board,num):
			return False
	else:
		return True

def player_Input(board,player):
	'''inputs position from users and validates whether the position is empty or not using position_check function'''
	choice = " "
	while((choice not in "1 2 3 4 5 6 7 8 9".split() or not  position_Check(board,int(choice)))):
		choice = input("{a}  what position do you want to choose from 1-9?".format(a=player))
	return int(choice)

def replay():
	'''boolean function:asks users for replay.for Y.... input returns True otherwise returns false'''
	decision = input("Do you want to play again????").lower()
	if decision[0] == 'y':
		return True



while True:
	'''main function for game.runs untill a the loop is  exited using break'''
	os.system('clear')
	print('        \t                   Welcome To                           ')
	print('          \t                TIC     TAC     TOE                           \n')
	time.sleep(.4)
	board=[' ']*10
	print('\t\t\t\t   _1|_2_|_3__')
	print('\t\t\t\t   _4|_5_|_6_')
	print('\t\t\t\t    7| 8 | 9 \n')
	name=inputPlayer()
	turn = go_first()
	print("{a} will go first".format(a=name[turn]))
	time.sleep(.3)
	game_on=True
	time.sleep(1)
	while game_on:
		if turn== "X":
			#player 1
			Display_board(board)
			status_fullboard=board_Full(board,position_Check)
			if winner_check(board, "O"):
				print("Congrats {a} is the winner".format(a=name["O"]))
				break
			if status_fullboard:
				print("oops!its a tie")
				break
			position=player_Input(board,name["X"])
			status_position=position_Check(board,position)
			if status_position == True:
				position_board(position, board, "X")
			
			turn="O"

			
		else:
			#player2
			Display_board(board)
			status_fullboard=board_Full(board,position_Check)
			if winner_check(board, "X"):
				print("congrats {a} is the winner".format(a=name["X"]))
				break
			if status_fullboard:
				print("oops!its a tie")
				break
			position=player_Input(board,name["O"])
			status_position=position_Check(board,position)
			if status_position == True:
				position_board(position, board, "O")
		
			turn="X"
	if replay():
		continue
	else:
		print("Thank You for playing Tic Tac Toe BY Noobie Noobie\n bye bye bye")
		time.sleep(.7)
		os.system('clear')
		break


