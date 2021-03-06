import numpy as np
import sys


class coordinates():
    def __init__(self, i, j):
        self.coor = np.array([i, j])
        if i < 0 or i > 7:
            self.coor = -1
        if j < 0 or j > 7:
            self.coor = -1
        return
    
    def chess_coordinates(self):
        int_char = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        return [int_char[self.coor], self.coor[0] + 1]
    
    def add(self, x):
        res = self.coor + x
        return coordinates(res[0], res[1])


king_moves = [np.array([0, 1]), np.array([1, 0]), np.array([1, 1]), np.array([1, -1])]


class piece():
    def __init__(self, i, j, color, name='123'):
        self.coordinate = coordinates(i, j)  # np.array [i, j]
        self.color = color  # 0 - white, 1 - black
        self.first_move = 0
        self.name = name


    def all_moves(self):
        pass


class pawn(piece):
    def all_moves(self):
        if self.color == 0:
            if self.first_move == 0:
                mvs = np.array([self.coordinate.add(np.array([i, 0])) for i in range(1, 3)])
                self.first_move = 1
            else:
                mvs = np.array([self.coordinate.add(np.array([i, 0])) for i in range(1, 2)])
        else:
            if self.first_move == 0:
                self.first_move = 1
                mvs = np.array([self.coordinate.add((-1)*np.array([i, 0])) for i in range(1, 3)])
            else:
                mvs = np.array([self.coordinate.add((-1)*np.array([i, 0])) for i in range(1, 2)])
        mvs = [m for m in mvs if m.coor != -1]
        return np.array(mvs)


class king(piece):
    def all_moves(self):
        global king_moves
        mvs = []
        for m in king_moves:
            mvs.append(self.coordinate.add(m))
            mvs.append(self.coordinate.add(m*(-1)))
        if self.first_move == 0:
            pass  # + рокировка
        mvs = [m for m in mvs if m.coor != -1]
        return np.array(mvs)


class queen(piece):
    def all_moves(self):
        global king_moves
        mvs = []
        for m in king_moves:
            for k in range(1, 8):
                mvs.append(self.coordinate.add(m*k))
                mvs.append(self.coordinate.add(m*k*(-1)))
        mvs = [m for m in mvs if m.coor != -1]
        return np.array(mvs)


class knight(piece):
    knight_moves = [np.array([2, 1]), np.array([1, 2]), np.array([-2, 1]), np.array([-1, 2])]

    def all_moves(self):
        #nonlocal knight_moves
        mvs = []
        for m in knight_moves:
            mvs.append(self.coordinate.add(m))
            mvs.append(self.coordinate.add(m*(-1)))
        mvs = [m for m in mvs if m.coor != -1]
        return np.array(mvs)


class rook(piece):
    def all_moves(self):
        mvs = []
        for k in range(1, 8):
            mvs.append(self.coordinate.add(np.array([1, 0]*k)))
            mvs.append(self.coordinate.add(np.array([0, 1]*k)))
            mvs.append(self.coordinate.add(np.array([-1, 0]*k)))
            mvs.append(self.coordinate.add(np.array([0, -1]*k)))
        mvs = [m for m in mvs if m.coor != -1]
        return np.array(mvs)


class bishop(piece):
    bishop_moves = [np.array([1, 1]), np.array([1, -1])]
    
    def all_moves(self):
        mvs = []
        for m in bishop_moves:
            for k in range(1, 8):
                mvs.append(self.coordinate.add(m*k))
                mvs.append(self.coordinate.add(-m*k))
        mvs = [m for m in mvs if m.coor != -1]
        return np.array(mvs)


class board():
    def __init__(self, pieces):  # pieces = {[1, 0, 0]: 'pawn', [1, 1, 0]: 'pawn', [0, 0, 0]: 'rook', [0, 1]: 'knight'}
       self.board = [
            eval(n+f'({i[0]}, {i[1]}, {i[2]}, n)') for i, n in pieces.items()  # pawn(1, 0, 0)
        ]

    def info(self):
        res = []
        for i in self.board:
            res.append((np.hstack([i.coordinate.coor, i.color]), i.name))
            print(i.name)
        return res

    def piece(self, coor):  # coor = [a, b]
        res = None
        for piece in self.board:
            if piece.coordinate.coor == coor:
                res = piece
        return res

    def possibleMoves(self, coord):
        for i in range(len(self.board)):
            if coord == self.board[i].coordinate.coor:
                current_piece = self.board[i]  # нашли фигуру
                piece_number = i  # её номер
                break
        pieces = self.info()
        pieces_coor = []
        for i in range(len(pieces)):
            pieces_coor.append(pieces[i][0][:2])
        pieces_coor = np.array(pieces_coor)
        all_moves = current_piece.all_moves()
        if current_piece.name == 'pawn':
            for m in all_moves:
                if m in pieces_coor:
                    b_piece = self.piece(m)





pieces = {(1, 0, 0): 'pawn', (1, 1, 0): 'pawn', (0, 0, 0): 'rook'}
myboard = board(pieces)
print(myboard.info())

