'''
This is a simple cli based tictactoe game.
'''
import random

def drawBoard(board):
	'''
	Drawing the board.
	'''
	print(" "+board[7]+"|"+board[8]+"|"+board[9])
	print(" ----- ")
	print(" "+board[4]+"|"+board[5]+"|"+board[6])
	print(" ----- ")
	print(" "+board[1]+"|"+board[2]+"|"+board[3])

def selectLetter():
	'''
	It gives the user choice to select X or O. Which ever they want to choose.
	'''
	letter=' '
	while not (letter=='X' or letter=='O'):
		print("Do You Want To Use X or O: ")
		letter=input().upper()
	if letter == "X":
		return ['X','O']
	else:
		return ['O','X']

def isEmpty(board,box):
	'''
	Check the given box in the board is empty or not. Gives result in True or False.
	'''
	return board[box].isdigit()

def selectTheBox(board,l):
	'''
	To take entry in the board and return list.
	'''
	n=' '
	while n not in '1 2 3 4 5 6 7 8 9'.split() or not isEmpty(board,int(n)):
		n=input("Enter Between 1-9: ")
	board[int(n)]=l
	return board

def winner(board,letter):
	if  ((board[7]==letter and board[8]==letter and board[9]==letter)or
		(board[4]==letter and board[5]==letter and board[6]==letter)or
		(board[1]==letter and board[2]==letter and board[3]==letter)or
		(board[7]==letter and board[4]==letter and board[1]==letter)or
		(board[5]==letter and board[8]==letter and board[2]==letter)or
		(board[9]==letter and board[6]==letter and board[9]==letter)or
		(board[7]==letter and board[5]==letter and board[3]==letter)or
		(board[1]==letter and board[5]==letter and board[9]==letter)):
			return True

def tie(board):
	for  i in range(1,10):
		if isEmpty(board,i):
			return False
	return True

def compSelectTheBox(board,letter):
	arr=[]
	for i in range(1,10):
		if isEmpty(board,i):
			arr.append(i)
	board[random.choice(arr)]=letter
	return board


def main():
	theBoard='0 1 2 3 4 5 6 7 8 9 '.split()
	drawBoard(theBoard)
	usrL,compL=selectLetter()

	if usrL == 'X':
		turn="user"
	else:
		turn="computer"

	while True:
		if turn == "user":
			print("User Turn :")
			theBoard=selectTheBox(theBoard,usrL)
			drawBoard(theBoard)
			turn="computer"
		elif turn == "computer":
			print("Computer Turn :")
			theBoard=compSelectTheBox(theBoard,compL)
			drawBoard(theBoard)
			turn="user"

		if winner(theBoard,usrL):
			print("You Win!! Congrats......")
			break
		elif winner(theBoard,compL):
			print("Sorry! You Loss. Computer Wins.")
			break
		elif tie(theBoard):
			print("It seem we have tie......")
			break


if __name__=='__main__':
	main()