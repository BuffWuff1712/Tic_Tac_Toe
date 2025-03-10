import tkinter as tk
from tkinter import messagebox
from backend.AI_Bot import AI_Bot

# Initialize AI Bot
ai_player = "O"
human_player = "X"
ai_bot = AI_Bot(ai_player, human_player)

# Initialize board
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"  # Default to human

# Function to check for a winner
def check_winner():
    result = ai_bot.evaluate(board)
    if result == 100:
        return ai_player
    elif result == -100:
        return human_player
    return None

# Function to check if the board is full (draw)
def is_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

# Function to handle player's move
def on_click(row, col):
    global current_player

    if board[row][col] == "" and not check_winner():
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
            return
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return

        # Switch to AI turn
        current_player = ai_player
        root.after(500, ai_move)  # Delay for AI move

# Function to handle AI's move
def ai_move():
    global current_player

    move = ai_bot.minimax(board, depth=0, max_depth=9, current_player=ai_player)
    if move:
        board[move[0]][move[1]] = ai_player
        buttons[move[0]][move[1]].config(text=ai_player)

    winner = check_winner()
    if winner:
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        reset_board()
        return
    elif is_draw():
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_board()
        return

    # Switch back to human player
    current_player = human_player

# Function to reset the game
def reset_board():
    global board, current_player

    # Reset board
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

    # Get selected first player
    selected_first_player = first_player_var.get()
    current_player = selected_first_player

    # AI moves first if selected
    if current_player == ai_player:
        root.after(500, ai_move)

# Create GUI window
root = tk.Tk()
root.title("Tic-Tac-Toe with AI")

# First Player Selection (Radio Buttons)
first_player_var = tk.StringVar(value=human_player)  # Default: Human starts
tk.Label(root, text="Who goes first?", font=("Arial", 14)).grid(row=0, column=0, columnspan=3)
tk.Radiobutton(root, text="Me", font=("Arial", 12), variable=first_player_var, value=human_player).grid(row=1, column=0, columnspan=1)
tk.Radiobutton(root, text="AI", font=("Arial", 12), variable=first_player_var, value=ai_player).grid(row=1, column=1, columnspan=1)

# Create Tic-Tac-Toe Grid
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                                  command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i + 2, column=j)  # Offset by 2 rows for first-player selection

# Reset Button
reset_button = tk.Button(root, text="Reset", font=("Arial", 15), command=reset_board)
reset_button.grid(row=5, column=0, columnspan=3)

# Run the GUI
root.mainloop()
