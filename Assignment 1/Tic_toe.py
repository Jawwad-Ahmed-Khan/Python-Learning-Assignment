import math

class TicTacToe:
    def __init__(self):

        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'O'

    def print_board(self):

        for row in self.board:
            print(' | '.join(cell if cell is not None else ' ' for cell in row))
            print('-' * 9)

    def available_moves(self):
        moves = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] is None:
                    moves.append((r, c))
        return moves

    def make_move(self, r, c, player):
        self.board[r][c] = player

    def undo_move(self, r, c):
        self.board[r][c] = None

    def winner(self):
        lines = []
        for i in range(3):
            lines.append(self.board[i])
            lines.append([self.board[r][i] for r in range(3)])
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2-i] for i in range(3)])

        for line in lines:
            if line[0] is not None and line.count(line[0]) == 3:
                return line[0]
        return None

    def is_full(self):
        return all(cell is not None for row in self.board for cell in row)

    def terminal_state(self):
        win = self.winner()
        if win == 'X':
            return True, +1
        elif win == 'O':
            return True, -1
        elif self.is_full():
            return True, 0
        else:
            return False, None

    def minimax(self, maximizing_player):
        terminal, utility = self.terminal_state()
        if terminal:
            return utility

        if maximizing_player:
            max_eval = -math.inf
            for (r, c) in self.available_moves():
                self.make_move(r, c, 'X')
                eval = self.minimax(False)
                self.undo_move(r, c)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = +math.inf
            for (r, c) in self.available_moves():
                self.make_move(r, c, 'O')
                eval = self.minimax(True)
                self.undo_move(r, c)
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self):
        best_val = -math.inf
        best_move = None
        for (r, c) in self.available_moves():
            self.make_move(r, c, 'X')
            move_val = self.minimax(False)
            self.undo_move(r, c)
            if move_val > best_val:
                best_val = move_val
                best_move = (r, c)
        return best_move

    def play(self):
        print("Welcome to Tic‑Tac‑Toe! You are O, AI is X.")
        self.print_board()

        while True:
            valid = False
            while not valid:
                try:
                    raw = input("Enter your move (row and column 0–2, e.g. '1 2'): ")
                    r, c = map(int, raw.split())
                    if (r, c) in self.available_moves():
                        valid = True
                    else:
                        print("Cell is occupied or out of range. Try again.")
                except Exception:
                    print("Invalid input. Try again.")
            self.make_move(r, c, 'O')
            self.print_board()

            terminal, utility = self.terminal_state()
            if terminal:
                if utility == -1:
                    print("You win! 🎉")
                elif utility == 0:
                    print("It's a draw.")
                return

            print("AI is thinking...")
            r_ai, c_ai = self.best_move()
            self.make_move(r_ai, c_ai, 'X')
            print(f"AI plays at {r_ai}, {c_ai}")
            self.print_board()

            terminal, utility = self.terminal_state()
            if terminal:
                if utility == +1:
                    print("AI wins! thr Tic Toe Game")
                elif utility == 0:
                    print("It's a draw.")
                return

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
