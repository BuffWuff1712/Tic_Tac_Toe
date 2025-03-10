import copy
import random

class AI_Bot:
    def __init__(self, player, opponent, difficulty="hard"):
        self.player = player
        self.opponent = opponent
        self.difficulty = difficulty  # "easy", "medium", or "hard"

    def generate_valid_moves(self, board):
        return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]

    def evaluate(self, board):
        score = 0
        lines = []

        # Add rows and columns
        for i in range(3):
            lines.append([board[i][0], board[i][1], board[i][2]])  # Row
            lines.append([board[0][i], board[1][i], board[2][i]])  # Column

        # Add diagonals
        lines.append([board[0][0], board[1][1], board[2][2]])  # Main diagonal
        lines.append([board[0][2], board[1][1], board[2][0]])  # Anti-diagonal

        for line in lines:
            if line.count(self.player) == 3:
                return 100
            elif line.count(self.opponent) == 3:
                return -100
            elif line.count(self.player) == 2 and line.count("") == 1:
                score += 10
            elif line.count(self.opponent) == 2 and line.count("") == 1:
                score -= 10
            elif line.count(self.player) == 1 and line.count("") == 2:
                score += 1
            elif line.count(self.opponent) == 1 and line.count("") == 2:
                score -= 1

        return score

    def is_game_over(self, board):
        return self.evaluate(board) in [100, -100] or all(board[i][j] != "" for i in range(3) for j in range(3))

    def make_move(self, board, move, current_player):
        new_board = copy.deepcopy(board)
        new_board[move[0]][move[1]] = current_player
        return new_board

    def minimax(self, board, depth=0, max_depth=9, current_player=None):
        if self.difficulty == "easy":
            return random.choice(self.generate_valid_moves(board))

        if self.difficulty == "medium":
            max_depth = 2  # Limited lookahead for medium difficulty

        def max_value(board, depth):
            if self.is_game_over(board) or depth == max_depth:
                return self.evaluate(board), None
            max_score, best_move = float("-inf"), None
            for move in self.generate_valid_moves(board):
                new_board = self.make_move(board, move, self.player)
                score, _ = min_value(new_board, depth + 1)
                if score > max_score:
                    max_score, best_move = score, move
            return max_score, best_move

        def min_value(board, depth):
            if self.is_game_over(board) or depth == max_depth:
                return self.evaluate(board), None
            min_score, best_move = float("inf"), None
            for move in self.generate_valid_moves(board):
                new_board = self.make_move(board, move, self.opponent)
                score, _ = max_value(new_board, depth + 1)
                if score < min_score:
                    min_score, best_move = score, move
            return min_score, best_move

        if current_player is None:
            current_player = self.player

        score, best_move = (
            max_value(board, depth) if current_player == self.player else min_value(board, depth)
        )

        # For medium mode, introduce slight randomness
        if self.difficulty == "medium" and random.random() < 0.2:
            return random.choice(self.generate_valid_moves(board))

        return best_move
