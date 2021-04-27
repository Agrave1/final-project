import random
import os
row_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
player_score = 0
computer_score = 0
checked_square = []
def welcome_screen():
    #Display opening to game with possibility to see instructions
    print("\t\t\tWelcome to Two Player Minesweeper!")
    print()
    question = input("Would you like to see the instructions? Enter Y or N ")
    question = str(question)
    instructions = open("Instructions.txt", "r")
    if question == "Y":
        print()
        print("INSTRUCTIONS: ")
        for line in instructions:
            print(line)
    else:
        print()
        print("Get ready to play!")
    print()
def game_grid():
    #Makes unfilled game board with no mines
    #Source: https://www.askpython.com/python/examples/create-minesweeper-using-python
    global n
    global game_board
    row_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("\t\t\tMINESWEEPER")
    print()
    line = "   "
    for i in range(n):
        line = line + "     " + str(i + 1)
    print(line)
    for row_number in range(n):
        line = "     "
        if row_number == 0:
            for column_number in range(n):
                line = line +"______"
            print(line)
        line = "     "
        for column_number in range(n):
            line = line + "|  " + str(game_board[row_number][column_number]) + "  "
        print(line + "|")
        line = "  " + str(row_letters[row_number]) + "  "
        for column_number in range(n):
            line = line + "|____" + " "
        print(line + "|")
    print()
def mine_positions():
    #Creates random mine positions for each game
    #Source: https://www.askpython.com/python/examples/create-minesweeper-using-python
    global solution_board
    global game_board
    global n
    mine_count = 0
    while mine_count < number_mines:
        mine_index = random.randint(0, n * n - 1)
        #Generates random position for each mine
        row_number = mine_index // n
        #Row index of mine
        column_number = mine_index % n
        #Column index of mine
        if solution_board[row_number][column_number] != -1:
            #Checks to make sure random square is not already mine
            #If it is new random square is generated if not square becomes mine
            mine_count += 1
            solution_board[row_number][column_number] = -1
def square_values():
    #Assigns values to sqaures based on number of bordering mines
    #Source: https://www.askpython.com/python/examples/create-minesweeper-using-python
    global solution_board
    global n
    for row_number in range(n):
        for column_number in range(n):
            if solution_board[row_number][column_number] == -1:
                #If square has a mine skip assigning value
                continue
            if row_number > 0 and solution_board[row_number - 1][column_number] == -1:
                #Checks square directly above
                solution_board[row_number][column_number] = solution_board[row_number][column_number] + 1
            if row_number < n - 1 and solution_board[row_number + 1][column_number] == -1:
                #Checks square directly below
                solution_board[row_number][column_number] = solution_board[row_number][column_number] + 1
            if column_number > 0 and solution_board[row_number][column_number - 1] == -1:
                # Checks square to left
                solution_board[row_number][column_number] = solution_board[row_number][column_number] + 1
            if column_number < n - 1 and solution_board[row_number][column_number + 1] == -1:
                #Checks square to right
                solution_board[row_number][column_number] = solution_board[row_number][column_number] + 1
            if row_number > 0 and column_number > 0 and solution_board[row_number - 1][column_number - 1] == -1:
                #Checks square to top-left
                solution_board[row_number][column_number] = solution_board[row_number][column_number] + 1
            if row_number > 0 and column_number < n - 1 and solution_board[row_number - 1][column_number + 1] == -1:
                #Checks square to top_right
                solution_board[row_number][column_number] = solution_board[row_number][column_number] + 1
            if row_number < n - 1 and column_number > 0 and solution_board[row_number + 1][column_number - 1] == -1:
                #Checks square to bottom_left
                solution_board[row_number][column_number] = solution_board[row_number][column_number] + 1
            if row_number < n - 1 and column_number < n - 1 and solution_board[row_number + 1][column_number + 1] == -1:
                #Checks square to bottom_right
                solution_board[row_number][column_number] = solution_board[row_number][column_number] + 1
def zero_values(row_number, column_number):
    #Function that deals with special case zero value
    #When zero value is chosen bordering squares have to be revealed until all are not zero
    #Source: https://www.askpython.com/python/examples/create-minesweeper-using-python
    global solution_board
    global game_board
    global checked_square
    if [row_number, column_number] not in checked_square:
        checked_square.append([row_number, column_number])
        if solution_board[row_number][column_number] == 0:
            game_board[row_number][column_number] = solution_board[row_number][column_number]
            if row_number > 0:
                zero_values((row_number - 1), column_number)
            if row_number < (n - 1):
                zero_values((row_number + 1), column_number)
            if column_number > 0:
                zero_values(row_number, (column_number - 1))
            if column_number < (n - 1):
                zero_values(row_number, (column_number + 1))
            if row_number > 0 and column_number > 0:
                zero_values((row_number - 1), (column_number - 1))
            if row_number > 0 and column_number < (n - 1):
                zero_values((row_number - 1), (column_number + 1))
            if row_number < (n - 1) and column_number > 0:
                zero_values((row_number + 1), (column_number - 1))
            if row_number < (n - 1) and column_number < (n - 1):
                zero_values((row_number + 1), (column_number + 1))
        if solution_board[row_number][column_number] != 0:
            game_board[row_number][column_number] = solution_board[row_number][column_number]
def clear():
    #Clears terminal
    #Source: https://www.askpython.com/python/examples/create-minesweeper-using-python
    os.system("clear")
def reminder():
    #Tells player how to enter input to play each move
    turn_instructions = open("Turn_Instructions.txt", "r")
    for line in turn_instructions:
        print(line)
def check_score():
    global player_score
    global computer_score
    if computer_score == 11:
        print("Game over, computer has won. Better luck next time.")
        return True
    if player_score == 11:
        print("Congratulations, you have won! Nice job!")
        return True
    else:
        return
def input_check(turn):
    row_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    column_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if len(turn) == 2:
        if turn[0] in row_letters and turn[1] in column_labels:
            return True
        return False
    if len(turn) == 3:
        if turn[0] in row_letters and turn[1] in column_labels and turn[2] == "F":
            return True
        else:
            return False
    else:
        return False
def player_turn():
    global flags
    global solution_board
    global game_board
    global player_score
    global computer_score
    global name
    global done
    global checked_square
    row_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    column_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    letter_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
    print()
    print("Player score: ", player_score)
    print("Computer score: ", computer_score)
    turn = input("Enter row letter as capital and column number seperated by a space: ").split()
    input_check(turn)
    if input_check == False:
        clear()
        print()
        print("INVALID INPUT")
        print()
        player_turn()
    else:
        row_number = letter_dictionary.get(turn[0])
        column_number = int(turn[1]) - 1
        #Get coordinates of input
        if game_board[row_number][column_number] != " ":
            #When not blank square has been chosen with a revealed value
            clear()
            print("Square already chosen. End of turn.")
            print()
            return
        if solution_board[row_number][column_number] == -1 and len(turn) == 2:
            #When -1 the square is a mine
            clear()
            print("Chose a mine without flagging. Point to computer.")
            print()
            flags.append([row_number, column_number])
            game_board[row_number][column_number] = "F"
            computer_score += 1
            if computer_score >= 11:
                print("Game over, computer has won. Better luck next time.")
                finished = True
                return
            return
        if solution_board[row_number][column_number] != -1 and solution_board[row_number][column_number] != 0 and len(turn) == 3:
            #Checks to make sure it isn't a mine and not a zero as well
            # Zero is a special value that requires extra steps
            clear()
            print("Not a mine, can't place flag. End of turn.")
            print()
            game_board[row_number][column_number] = solution_board[row_number][column_number]
            return
        if solution_board[row_number][column_number] == -1 and len(turn) == 3:
            #If square is -1 it is a mine
            clear()
            print("Flag set correctly, gained point.")
            flags.append([row_number, column_number])
            game_board[row_number][column_number] = "F"
            player_score += 1
            if player_score >= 11:
                print("Congratulations, you have won! Nice job!")
                finished = True
                return
            game_grid()
            player_turn()
            return
        if solution_board[row_number][column_number] == 0:
            game_board[row_number][column_number] == "0"
            zero_values(row_number, column_number)
        if game_board[row_number][column_number] == " ":
            game_board[row_number][column_number] = solution_board[row_number][column_number]
            return
def computer_turn():
    global player_score
    global computer_score
    global checked_square
    move = random.randint(0, n * n -1)
    #Generate random coordinates for move
    row_number = move // n
    column_number = move % n
    if solution_board[row_number][column_number] == -1:
            print("Computer flagged mine, gained point.")
            print("Computer chose row ", row_letters[row_number], "and column ", column_number + 1)
            flags.append([row_number, column_number])
            game_board[row_number][column_number] = "F"
            computer_score += 1
            if computer_score >= 11:
                print("Game over, computer has won. Better luck next time.")
                finished = True
                return
            computer_turn()
            return
    if game_board[row_number][column_number] == 1:
        clear()
        if row_number >= 1:
            if solution_board[row_number - 1][column_number] == -1 and game_board[row_number - 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 1)
                flags.append([row_number - 1, column_number])
                game_board[row_number - 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number <= 9:
            if solution_board[row_number - 1][column_number + 1] == -1 and game_board[row_number - 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 2)
                flags.append([row_number - 1, column_number + 1])
                game_board[row_number - 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number <= 9:
            if solution_board[row_number][column_number + 1] == -1 and game_board[row_number][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number + 2)
                flags.append([row_number, column_number + 1])
                game_board[row_number][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number <= 9:
            if solution_board[row_number + 1][column_number + 1] == -1 and game_board[row_number + 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number + 2)
                flags.append([row_number + 1, column_number + 1])
                game_board[row_number + 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9:
            if solution_board[row_number + 1][column_number] == -1 and game_board[row_number + 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number +1], "and column ", column_number + 1)
                flags.append(([row_number + 1, column_number]))
                game_board[row_number + 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number >= 1:
            if solution_board[row_number + 1][column_number - 1] == -1 and game_board[row_number + 1][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number)
                flags.append([row_number + 1, column_number - 1])
                game_board[row_number + 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number >= 1:
            if solution_board[row_number][column_number - 1] == -1 and game_board[row_number][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number)
                flags.append([row_number, column_number - 1])
                game_board[row_number][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number >= 1:
            if solution_board[row_number - 1][column_number - 1] == -1 and game_board[row_number - 1][column_number - 1] ==  " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number)
                flags.append([row_number - 1, column_number - 1])
                game_board[row_number - 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
    if game_board[row_number][column_number] == 2:
        clear()
        if row_number >= 1:
            if solution_board[row_number - 1][column_number] == -1 and game_board[row_number - 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 1)
                flags.append([row_number - 1, column_number])
                game_board[row_number - 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number <= 9:
            if solution_board[row_number - 1][column_number + 1] == -1 and game_board[row_number - 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 2)
                flags.append([row_number - 1, column_number + 1])
                game_board[row_number - 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number <= 9:
            if solution_board[row_number][column_number + 1] == -1 and game_board[row_number][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number + 2)
                flags.append([row_number, column_number + 1])
                game_board[row_number][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number <= 9:
            if solution_board[row_number + 1][column_number + 1] == -1 and game_board[row_number + 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number + 2)
                flags.append([row_number + 1, column_number + 1])
                game_board[row_number + 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9:
            if solution_board[row_number + 1][column_number] == -1 and game_board[row_number + 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number +1], "and column ", column_number + 1)
                flags.append(([row_number + 1, column_number]))
                game_board[row_number + 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number >= 1:
            if solution_board[row_number + 1][column_number - 1] == -1 and game_board[row_number + 1][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number)
                flags.append([row_number + 1, column_number - 1])
                game_board[row_number + 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number >= 1:
            if solution_board[row_number][column_number - 1] == -1 and game_board[row_number][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number)
                flags.append([row_number, column_number - 1])
                game_board[row_number][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number >= 1:
            if solution_board[row_number - 1][column_number - 1] == -1 and game_board[row_number - 1][column_number - 1] ==  " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number)
                flags.append([row_number - 1, column_number - 1])
                game_board[row_number - 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
    if game_board[row_number][column_number] == 3:
        clear()
        if row_number >= 1:
            if solution_board[row_number - 1][column_number] == -1 and game_board[row_number - 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 1)
                flags.append([row_number - 1, column_number])
                game_board[row_number - 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number <= 9:
            if solution_board[row_number - 1][column_number + 1] == -1 and game_board[row_number - 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 2)
                flags.append([row_number - 1, column_number + 1])
                game_board[row_number - 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number <= 9:
            if solution_board[row_number][column_number + 1] == -1 and game_board[row_number][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number + 2)
                flags.append([row_number, column_number + 1])
                game_board[row_number][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number <= 9:
            if solution_board[row_number + 1][column_number + 1] == -1 and game_board[row_number + 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number + 2)
                flags.append([row_number + 1, column_number + 1])
                game_board[row_number + 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9:
            if solution_board[row_number + 1][column_number] == -1 and game_board[row_number + 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number +1], "and column ", column_number + 1)
                flags.append(([row_number + 1, column_number]))
                game_board[row_number + 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number >= 1:
            if solution_board[row_number + 1][column_number - 1] == -1 and game_board[row_number + 1][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number)
                flags.append([row_number + 1, column_number - 1])
                game_board[row_number + 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number >= 1:
            if solution_board[row_number][column_number - 1] == -1 and game_board[row_number][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number)
                flags.append([row_number, column_number - 1])
                game_board[row_number][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number >= 1:
            if solution_board[row_number - 1][column_number - 1] == -1 and game_board[row_number - 1][column_number - 1] ==  " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number)
                flags.append([row_number - 1, column_number - 1])
                game_board[row_number - 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
    if game_board[row_number][column_number] == 4:
        clear()
        if row_number >= 1:
            if solution_board[row_number - 1][column_number] == -1 and game_board[row_number - 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 1)
                flags.append([row_number - 1, column_number])
                game_board[row_number - 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number <= 9:
            if solution_board[row_number - 1][column_number + 1] == -1 and game_board[row_number - 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 2)
                flags.append([row_number - 1, column_number + 1])
                game_board[row_number - 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number <= 9:
            if solution_board[row_number][column_number + 1] == -1 and game_board[row_number][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number + 2)
                flags.append([row_number, column_number + 1])
                game_board[row_number][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number <= 9:
            if solution_board[row_number + 1][column_number + 1] == -1 and game_board[row_number + 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number + 2)
                flags.append([row_number + 1, column_number + 1])
                game_board[row_number + 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9:
            if solution_board[row_number + 1][column_number] == -1 and game_board[row_number + 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number +1], "and column ", column_number + 1)
                flags.append(([row_number + 1, column_number]))
                game_board[row_number + 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number >= 1:
            if solution_board[row_number + 1][column_number - 1] == -1 and game_board[row_number + 1][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number)
                flags.append([row_number + 1, column_number - 1])
                game_board[row_number + 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number >= 1:
            if solution_board[row_number][column_number - 1] == -1 and game_board[row_number][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number)
                flags.append([row_number, column_number - 1])
                game_board[row_number][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number >= 1:
            if solution_board[row_number - 1][column_number - 1] == -1 and game_board[row_number - 1][column_number - 1] ==  " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number)
                flags.append([row_number - 1, column_number - 1])
                game_board[row_number - 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
    if game_board[row_number][column_number] == 5:
        clear()
        if row_number >= 1:
            if solution_board[row_number - 1][column_number] == -1 and game_board[row_number - 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 1)
                flags.append([row_number - 1, column_number])
                game_board[row_number - 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number <= 9:
            if solution_board[row_number - 1][column_number + 1] == -1 and game_board[row_number - 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 2)
                flags.append([row_number - 1, column_number + 1])
                game_board[row_number - 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number <= 9:
            if solution_board[row_number][column_number + 1] == -1 and game_board[row_number][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number + 2)
                flags.append([row_number, column_number + 1])
                game_board[row_number][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number <= 9:
            if solution_board[row_number + 1][column_number + 1] == -1 and game_board[row_number + 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number + 2)
                flags.append([row_number + 1, column_number + 1])
                game_board[row_number + 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9:
            if solution_board[row_number + 1][column_number] == -1 and game_board[row_number + 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number +1], "and column ", column_number + 1)
                flags.append(([row_number + 1, column_number]))
                game_board[row_number + 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number >= 1:
            if solution_board[row_number + 1][column_number - 1] == -1 and game_board[row_number + 1][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number)
                flags.append([row_number + 1, column_number - 1])
                game_board[row_number + 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number >= 1:
            if solution_board[row_number][column_number - 1] == -1 and game_board[row_number][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number)
                flags.append([row_number, column_number - 1])
                game_board[row_number][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number >= 1:
            if solution_board[row_number - 1][column_number - 1] == -1 and game_board[row_number - 1][column_number - 1] ==  " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number)
                flags.append([row_number - 1, column_number - 1])
                game_board[row_number - 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
    if game_board[row_number][column_number] == 6:
        clear()
        if row_number >= 1:
            if solution_board[row_number - 1][column_number] == -1 and game_board[row_number - 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 1)
                flags.append([row_number - 1, column_number])
                game_board[row_number - 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number <= 9:
            if solution_board[row_number - 1][column_number + 1] == -1 and game_board[row_number - 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 2)
                flags.append([row_number - 1, column_number + 1])
                game_board[row_number - 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number <= 9:
            if solution_board[row_number][column_number + 1] == -1 and game_board[row_number][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number + 2)
                flags.append([row_number, column_number + 1])
                game_board[row_number][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number <= 9:
            if solution_board[row_number + 1][column_number + 1] == -1 and game_board[row_number + 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number + 2)
                flags.append([row_number + 1, column_number + 1])
                game_board[row_number + 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9:
            if solution_board[row_number + 1][column_number] == -1 and game_board[row_number + 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number +1], "and column ", column_number + 1)
                flags.append(([row_number + 1, column_number]))
                game_board[row_number + 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number >= 1:
            if solution_board[row_number + 1][column_number - 1] == -1 and game_board[row_number + 1][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number)
                flags.append([row_number + 1, column_number - 1])
                game_board[row_number + 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number >= 1:
            if solution_board[row_number][column_number - 1] == -1 and game_board[row_number][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number)
                flags.append([row_number, column_number - 1])
                game_board[row_number][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number >= 1:
            if solution_board[row_number - 1][column_number - 1] == -1 and game_board[row_number - 1][column_number - 1] ==  " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number)
                flags.append([row_number - 1, column_number - 1])
                game_board[row_number - 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
    if game_board[row_number][column_number] == 7:
        clear()
        if row_number >= 1:
            if solution_board[row_number - 1][column_number] == -1 and game_board[row_number - 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 1)
                flags.append([row_number - 1, column_number])
                game_board[row_number - 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number <= 9:
            if solution_board[row_number - 1][column_number + 1] == -1 and game_board[row_number - 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 2)
                flags.append([row_number - 1, column_number + 1])
                game_board[row_number - 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number <= 9:
            if solution_board[row_number][column_number + 1] == -1 and game_board[row_number][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number + 2)
                flags.append([row_number, column_number + 1])
                game_board[row_number][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number <= 9:
            if solution_board[row_number + 1][column_number + 1] == -1 and game_board[row_number + 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number + 2)
                flags.append([row_number + 1, column_number + 1])
                game_board[row_number + 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9:
            if solution_board[row_number + 1][column_number] == -1 and game_board[row_number + 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number +1], "and column ", column_number + 1)
                flags.append(([row_number + 1, column_number]))
                game_board[row_number + 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number >= 1:
            if solution_board[row_number + 1][column_number - 1] == -1 and game_board[row_number + 1][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number)
                flags.append([row_number + 1, column_number - 1])
                game_board[row_number + 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number >= 1:
            if solution_board[row_number][column_number - 1] == -1 and game_board[row_number][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number)
                flags.append([row_number, column_number - 1])
                game_board[row_number][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number >= 1:
            if solution_board[row_number - 1][column_number - 1] == -1 and game_board[row_number - 1][column_number - 1] ==  " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number)
                flags.append([row_number - 1, column_number - 1])
                game_board[row_number - 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
    if game_board[row_number][column_number] == 8:
        clear()
        if row_number >= 1:
            if solution_board[row_number - 1][column_number] == -1 and game_board[row_number - 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 1)
                flags.append([row_number - 1, column_number])
                game_board[row_number - 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number <= 9:
            if solution_board[row_number - 1][column_number + 1] == -1 and game_board[row_number - 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number + 2)
                flags.append([row_number - 1, column_number + 1])
                game_board[row_number - 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number <= 9:
            if solution_board[row_number][column_number + 1] == -1 and game_board[row_number][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number + 2)
                flags.append([row_number, column_number + 1])
                game_board[row_number][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number <= 9:
            if solution_board[row_number + 1][column_number + 1] == -1 and game_board[row_number + 1][column_number + 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number + 2)
                flags.append([row_number + 1, column_number + 1])
                game_board[row_number + 1][column_number + 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9:
            if solution_board[row_number + 1][column_number] == -1 and game_board[row_number + 1][column_number] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number +1], "and column ", column_number + 1)
                flags.append(([row_number + 1, column_number]))
                game_board[row_number + 1][column_number] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number <= 9 and column_number >= 1:
            if solution_board[row_number + 1][column_number - 1] == -1 and game_board[row_number + 1][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number + 1], "and column ", column_number)
                flags.append([row_number + 1, column_number - 1])
                game_board[row_number + 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if column_number >= 1:
            if solution_board[row_number][column_number - 1] == -1 and game_board[row_number][column_number - 1] == " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number], "and column ", column_number)
                flags.append([row_number, column_number - 1])
                game_board[row_number][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
        if row_number >= 1 and column_number >= 1:
            if solution_board[row_number - 1][column_number - 1] == -1 and game_board[row_number - 1][column_number - 1] ==  " ":
                print("Computer flagged mine, gained point.")
                print("Computer chose row ", row_letters[row_number - 1], "and column ", column_number)
                flags.append([row_number - 1, column_number - 1])
                game_board[row_number - 1][column_number - 1] = "F"
                computer_score += 1
                if computer_score >= 11:
                    print("Game over, computer has won. Better luck next time.")
                    finished = True
                    return
                computer_turn()
                return
    if solution_board[row_number][column_number] == 0:
        print("Computer chose row ", row_letters[row_number], "and column ", column_number + 1)
        game_board[row_number][column_number] == "0"
        zero_values(row_number, column_number)
    if game_board[row_number][column_number] == " ":
        print("Computer chose row ", row_letters[row_number], "and column ", column_number + 1)
        game_board[row_number][column_number] = solution_board[row_number][column_number]
        return
    if game_board[row_number][column_number] != " ":
        print("Computer chose already chosen square. End of turn.")
        return
if __name__ == "__main__":
    n = 10
    number_mines = 21
    solution_board = [[0 for y in range(n)] for x in range(n)]
    #Actual row values
    game_board = [[" " for y in range(n)] for x in range(n)]
    #Apparent row values(What has been revealed so far)
    flags = []
    #Flagged positions
    welcome_screen()
    mine_positions()
    square_values()
    clear()
    finished = False
    while not finished:
        game_grid()
        reminder()
        player_turn()
        computer_turn()
        if check_score() == True:
            finished = True
