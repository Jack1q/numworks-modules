# Othello / Reversi game
import random
class Move:
    def __init__(self, row:int, column:int):
        self.row = row
        self.column = column
        
class Othello:
    board = [['-' for x in range(8)] for y in range(8)]
    board[3][3] = 'W'
    board[3][4] = 'B'
    board[4][3] = 'B'
    board[4][4] = 'W'

    def make_move(self, row, column, marker):
        self.board[row][column] = marker
        temp = [self.board[x].copy() for x in range(8)]
        opponent_marker = 'W' if marker == 'B' else 'B'
        
        # Look below
        i = row + 1
        while i < 8 and self.board[i][column] == opponent_marker:
            i += 1
        if i < 8 and self.board[i][column] == marker:
            for x in range(row, i):
                temp[x][column] = marker
        # Look left
        j = column - 1
        while j > 0 and self.board[row][j] == opponent_marker:
            j -= 1
        if j >= 0 and self.board[row][j] == marker:
            for x in range(j, column):
                temp[row][x] = marker
        # Look Below Left
        i = row + 1
        j = column - 1
        while i < 8 and j > 0 and self.board[i][j] == opponent_marker:
            i += 1
            j -= 1
        if i < 8 and j >= 0 and self.board[i][j] == marker:
            next_row = i
            next_col = j
            while next_row > row and next_col < column:
                temp[next_row][next_col] = marker
                next_row -= 1
                next_col += 1
        # Look right
        j = column + 1
        while j < 8 and self.board[row][j] == opponent_marker:
            j += 1
        if j < 8 and self.board[row][j] == marker:
            for x in range(column, j):
                temp[row][x] = marker
        # Below Right
        i = row + 1
        j = column + 1
        while i < 7 and j < 8 and self.board[i][j] == opponent_marker: 
            i += 1
            j += 1
        if i < 8 and j < 8 and self.board[i][j] == marker:
            k = row
            l = column
            while k < i and l < j:
                temp[k][l] = marker
                k += 1
                l += 1
        # Above
        i = row - 1
        while i > 0 and self.board[i][column] == opponent_marker:
            i -= 1
        if i >= 0 and self.board[i][column] == marker:
            for x in range(i, row):
                temp[x][column] = marker
        # Above Left
        i = row - 1
        j = column - 1
        while i > 0 and j > 0 and self.board[i][j] == opponent_marker:
            j -= 1
            i -= 1
        if i >= 0 and j >= 0 and self.board[i][j] == marker:
            k = i
            l = j
            while k < row and l < column:
                temp[k][l] = marker
                k += 1
                l += 1
        # Above right
        i = row - 1
        j = column + 1
        while i > 0 and j < 8 and self.board[i][j] == opponent_marker:
            i -= 1
            j += 1
        if i >= 0 and j < 8 and self.board[i][j] == marker:
            k = i
            l = j
            while k < row and l > column:
                temp[k][l] = marker
                k += 1
                l -= 1
        self.board = [temp[x].copy() for x in range(8)]

    def get_possible_moves_for_piece(self, row, column, marker):
        moves = []
        opponent_marker = 'W' if marker == 'B' else 'B'
        # Up
        i = row - 1
        if i >= 0 and self.board[i][column] == opponent_marker:
            while i > 0 and self.board[i][column] == opponent_marker:
                i -= 1
            if i >= 0 and self.board[i][column] == '-':
                moves.append(Move(i, column))
        # Down
        i = row + 1
        if i < 8 and self.board[i][column] == opponent_marker:
            while i < 8 and self.board[i][column] == opponent_marker:
                i += 1
            if i < 8 and self.board[i][column] == '-':
                moves.append(Move(i, column))
        # Left
        j = column - 1
        if j > 0 and self.board[row][j] == opponent_marker:
            while j > 0 and self.board[row][j] == opponent_marker:
                j -= 1
            if j >= 0 and self.board[row][j] == '-':
                moves.append(Move(row, j))
        # Right
        j = column + 1
        if j < 8 and self.board[row][j] == opponent_marker:
            while j < 8 and self.board[row][j] == opponent_marker:
                j += 1
            if j < 8 and self.board[row][j] == '-':
                moves.append(Move(row, j))
        # Up Left
        i = row - 1
        j = column - 1
        if i >= 0 and j >= 0 and self.board[i][j] == opponent_marker:
            while j > 0 and i > 0 and self.board[i][j] == opponent_marker:
                j -= 1
                i -= 1
            if j >= 0 and i >= 0 and self.board[i][j] == '-':
                moves.append(Move(i, j))
        # Up Right
        i = row - 1
        j = column + 1
        if i >= 0 and j < 8 and self.board[i][j] == opponent_marker:
            while i > 0 and j < 8 and self.board[i][j] == opponent_marker:
                i -= 1
                j += 1
            if i >= 0 and j < 8 and self.board[i][j] == '-':
                moves.append(Move(i, j))
        # Down left
        i = row + 1
        j = column - 1
        if i < 8 and j >= 0 and self.board[i][j] == opponent_marker:
            while j > 0 and i < 8 and self.board[i][j] == opponent_marker:
                i += 1
                j -= 1
            if i < 8 and j >= 0 and self.board[i][j] == '-':
                moves.append(Move(i, j))
        # Down Right
        i = row + 1
        j = column + 1
        if i < 8 and j < 8 and self.board[i][j] == opponent_marker:
            while j < 8 and i < 8 and self.board[i][j] == opponent_marker:
                j += 1
                i += 1
            if i < 8 and j < 8 and self.board[i][j] == '-':
                moves.append(Move(i, j))
        return moves

    def get_possible_moves(self, marker):
        moves = []
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == marker:
                    piece_moves = self.get_possible_moves_for_piece(x, y, marker)
                    for z in piece_moves:
                        moves.append(z)
        return moves
        
    def show_board(self, marker):
        possible_moves = self.get_possible_moves(marker)
        for move in possible_moves:
            self.board[move.row][move.column] = '*'
        print('   0 1 2 3 4 5 6 7')
        for x in range(8):
            print(str(x) + ': ',end='')
            for y in range(8):
                print(self.board[x][y],end=' ')
                if self.board[x][y] == '*':
                    self.board[x][y] = '-'
            print('')

    def get_winner(self):
        w = 0
        b = 0
        for x in self.board:
            for y in self.board[x]:
                if y == 'W':
                    w += 1
                elif y == 'B':
                    b += 1
        if w > b:
            return 'White Wins'
        elif b > w:
            return 'Black Wins'
        else:
            return 'Tie'
    
    def has_moves_left(self, marker):
        return len(self.get_possible_moves(marker)) > 0
    
    def make_random_move(self, marker):
        possible_moves = self.get_possible_moves(marker)
        move = possible_moves[random.randint(0, len(possible_moves) - 1)]
        self.make_move(move.row, move.column, marker)

    def get_possible_moves_as_tuple(self, marker):
        return [(move.row, move.column) for move in self.get_possible_moves(marker)]

    def game(self):
        marker = input('W or B: ')
        while marker != 'W' and marker != 'B':
            marker = input('W or B: ')
        opponent_marker = 'W' if marker == 'B' else 'B'
        while self.has_moves_left(marker):
            self.show_board(marker)
            try:
                row = int(input('Row: '))
                col = int(input('Column: '))
                if (row, col) in self.get_possible_moves_as_tuple(marker):
                    self.make_move(row, col, marker)
                    if not(self.has_moves_left(marker)):
                        break
                    self.make_random_move(opponent_marker)
            except:
                pass
        winner = self.get_winner()
        print(winner)

if __name__ == '__main__':
    Othello().game()
