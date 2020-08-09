# Tic tac toe I made on my numworks calculator while on a train
# Made by Jack Donofrio
import random
class TicTacToe:
    board = [['-' for x in range(3)] for y in range(3)]
    def show_board(self):
        print('   0 1 2')
        for x in range(3):
            print(str(x) + ': ',end='')
            for y in range(3):
                print(self.board[x][y], end=' ')
            print()

    def make_move(self, row, column, marker:str):
        self.board[row][column] = marker

    def make_opponent_move(self, opponent_marker):
        moves = []
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == '-':
                    moves.append((x,y))
        move = moves[random.randint(0, len(moves) - 1)]
        self.board[move[0]][move[1]] = opponent_marker

    def move_is_valid(self, row, column):
        return row >= 0 and row < 3 and column >= 0 and column < 3 and self.board[row][column] == '-'
    
    def check_if_winner(self):
        for x in range(3):
            if self.board[x][0] != '-' and self.board[x][0] == self.board[x][1] == self.board[x][2]:
                return self.board[x][0]
            if self.board[0][x] != '-' and self.board[0][x] == self.board[1][x] == self.board[2][x]:
                return self.board[0][x]
            if self.board[1][1] != '-' and (self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == self.board[2][0]):
                return self.board[1][1]
        for x in range(3):
            if '-' in self.board[x]:
                return 'N'
        return 'Tie'

    def game(self):
        player_marker = ''
        while player_marker != 'X' and player_marker != 'O':
            player_marker = input('Enter X or O: ')
        opponent_marker = 'X' if player_marker == 'O' else 'O'
        while self.check_if_winner() == 'N':
            self.show_board()
            player_row = int(input('Enter row: '))
            player_col = int(input('Enter column: '))
            while not(self.move_is_valid(player_row, player_col)):
                player_row = int(input('Enter row: '))
                player_col = int(input('Enter column: '))
            self.make_move(player_row, player_col, player_marker)
            if self.check_if_winner() != 'N':
                break
            self.make_opponent_move(opponent_marker)
        self.show_board()
        winner = self.check_if_winner()
        if winner == 'Tie':
            print('Tie')
        else:
            print(winner, 'wins.')

if __name__ == '__main__':
    game = TicTacToe()
    game.game()