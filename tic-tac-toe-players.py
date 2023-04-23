import sys
from tkinter import *
from tkinter import messagebox
import os.path

# Define a function to create a player account


def create_account():
    player_name = input("Enter your name: ").strip().lower()
    while True:
        player_symbol = input(
            "Enter 'X' or 'O' as your symbol: ").strip().upper()
        if player_symbol in ["X", "O"]:
            break
        else:
            print("Invalid symbol. Please try again.")
    player_stats = [0, 0, 0]  # [wins, losses, ties]
    player_record = f"{player_name},{player_symbol},{player_stats[0]},{player_stats[1]},{player_stats[2]}\n"
    with open("tic-tac-toe-players.py", "a") as file:
        file.write(player_record)
    print("Account created successfully!")


# Define a function to display player stats
def display_stats(player):
    print(
        f"\nPlayer Name: {player[0].capitalize()}\nSymbol: {player[1]}\nWins: {player[2]}\nLosses: {player[3]}\nTies: {player[4]}")


# Define a function to update player stats
def update_stats(player, result):
    with open("tic-tac-toe-players.py", "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if player[0] in lines[i]:
            current_stats = lines[i].strip().split(",")
            if result == "win":
                current_stats[2] = str(int(current_stats[2]) + 1)
            elif result == "loss":
                current_stats[3] = str(int(current_stats[3]) + 1)
            else:
                current_stats[4] = str(int(current_stats[4]) + 1)
            updated_record = f"{current_stats[0]},{current_stats[1]},{current_stats[2]},{current_stats[3]},{current_stats[4]}\n"
            lines[i] = updated_record
            break

    with open("tic-tac-toe-players.py", "w") as file:
        file.writelines(lines)


# Main function to manage player accounts
def manage_accounts():
    # Check if the players file exists, create one if it doesn't
    if not os.path.exists("tic-tac-toe-players.py"):
        with open("tic-tac-toe-players.py", "w") as file:
            file.write("")

    while True:
        user_choice = input('''1. Create account
2. View stats
3. Start game
4. Quit
Enter your choice: ''').strip()

        if user_choice == "1":
            create_account()
        elif user_choice == "2":
            player_name = input("Enter your name: ").strip().lower()
            with open("tic-tac-toe-players.py", "r") as file:
                lines = file.readlines()
            player_found = False
            for line in lines:
                player = line.strip().split(",")
                if player[0] == player_name:
                    player_found = True
                    display_stats(player)
                    break
            if not player_found:
                print("Player not found. Please create an account first.")
        elif user_choice == "3":
            break
        elif user_choice == "4":
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manage_accounts()

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
            messagebox.showinfo("Game Over", "Player 1 Wins!")
        elif winner == "O":
            messagebox.showinfo("Game Over", "Player 2 Wins!")
        else:
            messagebox.showinfo("Game Over", "Tie Game!")

# function to make a move


def make_move(player, position):
    global board
    board[position] = player
    canvas.create_text((position % 3) * 100 + 50, (position // 3)
                       * 100 + 50, text=player, font=("Arial", 80), fill="red")

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
            if len([x for x in board if x != " "]) % 2 == 0:
                make_move("O", position)
            else:
                make_move("X", position)
            check_win(board[position])


# add the restart button
button = Button(root)
button = Button(root, text="Restart", command=restart_game)
button.pack()
canvas.bind("<Button-1>", click)
root.mainloop()
