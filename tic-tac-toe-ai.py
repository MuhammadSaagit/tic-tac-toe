from tkinter import *
import random
from tkinter import messagebox

# initialize the game board
board = [" "]*9

# initialize the game window
root = Tk()
root.title("Tic Tac Toe")

# initialize the game canvas
canvas = Canvas(root, width=300, height=300)
canvas.pack()

# draw the game grid on the canvas
canvas.create_line(100, 0, 100, 300, width=2)
canvas.create_line(200, 0, 200, 300, width=2)
canvas.create_line(0, 100, 300, 100, width=2)
canvas.create_line(0, 200, 300, 200, width=2)

# initialize the game status
game_over = False
winner = ""

# function to check for a winner


def check_win(player):
    global game_over
    global winner
    if (board[0] == board[1] == board[2] != " " or
        board[3] == board[4] == board[5] != " " or
        board[6] == board[7] == board[8] != " " or
        board[0] == board[3] == board[6] != " " or
        board[1] == board[4] == board[7] != " " or
        board[2] == board[5] == board[8] != " " or
        board[0] == board[4] == board[8] != " " or
            board[2] == board[4] == board[6] != " "):
        game_over = True
        winner = player
        if winner == "X":
            messagebox.showinfo("Game Over", "You Win!")
        elif winner == "O":
            messagebox.showinfo("Game Over", "You Lose!")
        else:
            messagebox.showinfo("Game Over", "Tie Game!")

# function to make a move


def make_move(player, position):
    global board
    board[position] = player
    canvas.create_text((position % 3) * 100 + 50, (position // 3)
                       * 100 + 50, text=player, font=("Arial", 80), fill="red")

# function for the AI to make a move


def ai_move():
    global board
    open_spots = [i for i in range(9) if board[i] == " "]
    if open_spots:
        position = random.choice(open_spots)
        make_move("O", position)
        check_win("O")

# function to restart the game


def restart_game():
    global board, game_over, winner
    board = [" "]*9
    canvas.delete("all")
    # Recreate the game grid
    canvas.create_line(100, 0, 100, 300, width=2)
    canvas.create_line(200, 0, 200, 300, width=2)
    canvas.create_line(0, 100, 300, 100, width=2)
    canvas.create_line(0, 200, 300, 200, width=2)
    game_over = False
    winner = ""

# event handler for mouse click


def click(event):
    global game_over
    if not game_over:
        x = event.x // 100
        y = event.y // 100
        position = y * 3 + x
        if board[position] == " ":
            make_move("X", position)
            check_win("X")
            if not game_over:
                ai_move()


# add the restart button
button = Button(root)
button = Button(root, text="Restart", command=restart_game)
button.pack()
canvas.bind("<Button-1>", click)
root.mainloop()
