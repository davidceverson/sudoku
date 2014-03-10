#!/usr/bin/python

#
# sudoku.py -- simple sudoku puzzle solver
#
# who                             when       why
# ------------------------------- ---------- ----------------------------------------
# david.c.everson@gmail.com       03-07-2014 initial development
#

import sys

# declare the 9x9 tableau -- input should be 9 rows of 9 digits separated by one blank
tableau = []

# global iteration counter
count = 0

# function defs

def setCell(r, c):
    """set the value of a cell -- recursively call self for next cell if this value is valid"""

    global tableau
    global count

    if r >= 9 and c >= 9:
        return True

    next_r, next_c = nextCell(r, c)
    #print "next_r: {} next_c: {}".format(next_r, next_c)

    if tableau[r][c] > 0:
        return setCell(next_r, next_c)
    else:
        for v in range(1, 10):
            if testRow(r, c, v) and testCol(r, c, v) and testSquare(r, c, v):
                count = count + 1
                #print "count: {} r: {} c: {} v: {}".format(count, r, c, v)
                tableau[r][c] = v

                if setCell(next_r, next_c):
                    return True
                else:
                    continue

        tableau[r][c] = 0

    return False

def testRow(r, c, v):
    """test if value v already exists in this row"""

    global tableau

    for k in range(9):
        if tableau[r][k] == v:
            return False
    return True

def testCol(r, c, v):
    """test if value v already exists in this column"""

    global tableau

    for k in range(9):
        if tableau[k][c] == v:
            return False
    return True

def testSquare(r, c, v):
    """test if the value v already exists in this sub-area (3x3) of the tableau"""

    global tableau

    R = (r // 3) * 3
    C = (c // 3) * 3
    for m in range(R, R + 2):
        for n in range (C, C + 2):
            if tableau[m][n] == v:
                return False

    return True

def nextCell(r, c):
    """return the row r and column c of the next cell in descending left-right order from the NW corner"""

    if r == 8 and c == 8: # at SE corner -- all done
        return 9, 9

    if r <= 8 and c < 8: # move one cell to the right
        c = c + 1
        return r, c

    if r < 8 and c == 8: # move to the left-most cell of the next row
        c = 0
        r = r + 1
        return r, c

    return r, c # this should never happen

def main():
    """Main driver routine -- executed if this module is called directly as a script"""
    global tableau

    # read input from stdin
    for line in sys.stdin:
        tableau.append(line.split())

    tableau = [[int(i) for i in line] for line in tableau] # convert input chars to ints

   # print starting tableau
    for line in tableau:
        print "{} ".format(line)

    if setCell(0, 0): # start at NW corner -- this will recursively call itself until it gets to the SE corner or fails
        print "\nSuccess!\n"
    else:
        print "\nFailed!\n"

    # print final tableau
    for line in tableau:
        print "{} ".format(line)

    print "\niteration count: {}".format(count)

# main sentinel
if __name__ == '__main__':
    main()

