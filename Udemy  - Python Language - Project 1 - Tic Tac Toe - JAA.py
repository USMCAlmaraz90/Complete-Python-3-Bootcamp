#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Write a function that can print out a board. Set up your board as a list, 
# where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

# This function is to display a board of up to 9 inputs. This board will display a manaully printed spaces and lines, 
# while adding the input spots (board[#]) and the spaces between each input


# In[2]:


from IPython.display import clear_output

def display_board(board):
     
# 1) create a function that will input a list
# 2) define the list input in the function (board)
# 3) create a board display manually that will make it asthetically pleasing to see each board input index

    print(" " + board[1] + '  |  ' + board[2] + '  |  ' + board [3] + "                1" + '  |  ' + "2" + '  |  ' + '3')
    print("---------------            ------------------")
    print(" " + board[4] + '  |  ' + board[5] + '  |  ' + board [6] + "                4" + '  |  ' + "5" + '  |  ' + '6')
    print("---------------            -------------------")
    print(" " + board[7] + '  |  ' + board[8] + '  |  ' + board [9] + "                7" + '  |  ' + "8" + '  |  ' + '9')


# In[3]:


#TEST Step 1: run your function on a test version of the board list, and make adjustments as necessary


# In[4]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board) 
# 1) create a list of items to test the board display, the list will run through the display_board function
# 2) the inputs will take a indexed spot according to the display_function(board) function.
# 3) The test_board must contain a list of 10 objects since our board is indexing for 1-9, and index starts at 0


# In[5]:


#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
# Think about using while loops to continually ask until you get a correct answer.


# In[6]:


# Now that we have a function that displays a board and can take in inputs, 
#we need to make a function that allows a player to choose a marker

def player_input():
    # Define a string to be defined for the X and O markers.  
    marker = ''
    # create a loop that will wait on a person to enter either X or O as a choice.
    # The input by a person has to accept lower case letters and turn it into an upper case. 
    while not (marker == "X" or marker == "O"):
        #The marker input must only be ONE equal sign (=) since it is a input variable that will be entered by a customer.
        # input variables will display a string to communicate to person what is being asked. 
        # if the input by a person does not equal to any of the markers, the while loop will ensure it keeps 
        # asking the person until a valid input is entered
            marker = input("Player 1, choose X or O as your marker:  ").upper()
        # once a marker is entered that breaks the loop, meaning a person chose X or x or O or o, then it will return
            if marker == "X":
                return ("X", "O")
            else:
                return ("O" , "X")


# In[7]:


#TEST Step 2: run the function to make sure it returns the desired output


# In[ ]:





# In[8]:


# Step 3: Write a function that takes in the board list object, 
    # a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.


# In[9]:


# the function will go to the board list in the display_board function, 
#it will index at a position, then equate a marker input to the positon

def place_marker(board, marker, position):
    board[position] = marker


# In[10]:


#TEST Step 3: run the place marker function using test parameters and display the modified board


# In[11]:


#This test will take the test_board list, and place a $ sign in position 8
place_marker(test_board,'$',8)
display_board(test_board)


# In[12]:


# Step 4: Write a function that takes in a board and checks to see if someone has won.


# In[13]:


# the function will take a board, and a see if a specific mark equals to each in each position,
# according to how you win.
# The function can just use the return function will default to say true or false if any criteria matches to the parameters
# it has to be a an OR between each, to ensure that only one scenerio occurs during a move. 
# the "mark" parameter is new since, a marker will check if X or O wins, 
# which is different than the input marker of a person
def win_check(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[1] == mark and board[4] == mark and board[7] == mark) or 
    (board[2] == mark and board[5] == mark and board[8] == mark) or 
    (board[3] == mark and board[6] == mark and board[9] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark) or 
    (board[3] == mark and board[5] == mark and board[7] == mark)) 


# In[14]:


#win_check(test_board,'X')


# In[15]:


#This function is checking if the 
win_check(test_board,'X')


# In[16]:


#Step 5: Write a function that uses the random module to randomly decide which player goes first. 
#You may want to lookup random.randint() Return a string of which player went first.


# In[17]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 2"
    else: 
        return "Player 1"


# In[18]:


#Step 6: Write a function that returns a boolean 
#indicating whether a space on the board is freely available.


# In[19]:


def space_check(board, position):
    return board[position] == ' '


# In[20]:


#Step 7: Write a function that checks if the board is full and returns a boolean value. 
    #True if full, False otherwise.


# In[21]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[22]:


#Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. 
#If it is, then return the position for later use. 


# In[23]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position (1-9): ' ))
    return position


# In[24]:


#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.


# In[25]:


def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')


# In[26]:


#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == "y":
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 has WON!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    print(" ")
                    print("               PLAYER 2's TURN", "(", player2_marker, ")")
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has WON!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    print(" ")
                    print("               PLAYER 1's TURN", "(", player1_marker, ")")
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





# In[ ]:




