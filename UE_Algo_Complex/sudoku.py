from re import S
import numpy as np
sudoku = np.loadtxt('sudoku.txt')
vide = np.where(sudoku == 0)
trouve = False

def acceptable(sudoku, x, y, e):
    pos_x = (x//3)*3
    pos_y = (y//3)*3
    tab=np.reshape(sudoku [pos_x : pos_x+3, pos_y : pos_y +3], (9))
    return (e not in sudoku[x] and e not in sudoku[:,y] and e not in tab)


def sudoCul(sudoku, vide, num):
    global trouve
    if num==len(vide[0]):
        trouve=True 
        return
    for e in range(1,10) :
        x = vide[0][num]
        y = vide[1][num]
        if acceptable(sudoku, x, y, e):
            sudoku[x,y] = e
            sudoCul(sudoku, vide, num+1)
            if trouve :
                return sudoku
            sudoku[x, y]= 0

print(sudoCul(sudoku, vide, 0))