import numpy as np


king_moves = [[0, 1], [1, 0], [1, 1], [-1, 1]]

class coordinates():
    def __init__(self, i, j):
        if i < 0 or i > 7:
            return -1
        if j < 0 or j > 7:
            return -1
        self.coor = np.array([i, j])
        return
    
    def chess_coordinates(self):
        int_char = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        return [int_char[self.coor], self.coor[0] + 1]
    
    def __add__(self, other):
        res = self.coor + other.coor
        return coordinates(res[0], res[1])
    
    def mul(self, i):
        res = self.coor*i
        return coordinates(res[0], res[1])

    def __sub__(self, other):
        return self + other.mul(-1)


class piece():
    def __init__(self, i, j, color):
        self.coordinate = coordinates(i, j) # np.array [i, j]
        self.color = color # 0 - white, 1 - black
        self.first_move = 0

    def all_moves(self):
        pass


class pawn(piece):
    def all_moves(self):
        if self.color == 0:
            if self.first_move == 0:
                mvs = np.array([self.coordinate + coordinates(i, 0) for i in range(1, 3)])
                self.first_move = 1
            else:
                mvs = np.array([self.coordinate + coordinates(i, 0) for i in range(1, 2)])
        else:
            if self.first_move == 0:
                self.first_move = 1
                mvs = np.array([self.coordinate - coordinates(i, 0) for i in range(1, 3)])
            else:
                mvs = np.array([self.coordinate - coordinates(i, 0) for i in range(1, 2)])
        mvs = [m for m in mvs if m != -1]
        return np.array(mvs)


class king(piece):
    def all_moves(self):
        global king_moves
        mvs = []
        for m in king_moves:
                mvs.append(self.coordinate + m)
                mvs.append(self.coordinate - m)
        if self.first_move == 0:
            pass  # + рокировка
        mvs = [m for m in mvs if m != -1]
        return np.array(mvs)


class queen(piece):
    def all_


class board():
    def __init__(self):
        self.board = [
            d
        ]