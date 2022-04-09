'''
Author: Clayton Branstetter
KUID: 3089206
Date: 04/01/2022
Lab: lab#06
Last modified: 04/08/2022
Purpose: Blob in the City: Backtracking and Recursion
'''

def move(mapchars, numRows, numCols, startR, startC, sewers, eaten, visited=[]):
    """move the blob to (startR, startC) if it's possible"""
    if (not ((0 <= startR < numRows) and (0 <= startC < numCols))):
        return 0

    visited.append((startR, startC)) # add (startR, startC) to the visited cells
    char = mapchars[startR][startC]

    if char == 'S': # Streets
        mapchars[startR][startC] = 'B'

    elif char == "#": # Buildings
        return 0

    elif char == "P": # People
        mapchars[startR][startC] = 'B'
        eaten[0] += 1

    elif char == "@": #Sewers
        for (x,y) in sewers:
            if (x,y) != (startR,startC): # next sewer
                if x == startR or y == startC:
                    sewers.remove((startR,startC))
                    # move to the next sewer
                    move(mapchars, numRows, numCols, x, y, sewers, eaten,visited=visited)
    # all directions
    directions = [(startR + 1, startC), (startR, startC + 1), (startR - 1, startC), (startR, startC - 1)]
    for direction in directions:
        if direction not in visited:
            # move to the next cell
            move(mapchars, numRows, numCols, direction[0], direction[1], sewers, eaten = eaten,visited=visited)


def main():
    file = input("enter the file name : ")
    try:
        with open(file, "r") as f: # open the file
            content = f.read()
        list_text = content.split('\n')
        cols_rows = list_text[0].split() # store numRows, numCols in a list
        numRows = int(cols_rows[0])

        if numRows < 1:
            raise Exception("numRows are less than 1")

        numCols = int(cols_rows[1])
        if numCols < 1:
            raise Exception("numCols are less than 1")

        starts = list_text[1].split() # store startRow, startCol in a list
        startRow = int(starts[0])
        startCol = int(starts[1])
        if not (0<=startRow<=numRows and 0<=startCol<=numCols):
            raise Exception("start position is not within range")

        maplist = list_text[2:] # read the map
        mapchars = [list(maplist[i]) for i in range(numRows)]
        # get all the sewers
        sewers = sum([[(i,j) for j in range(numCols) if mapchars[i][j] == '@'] for i in range(numRows)],[])
        eaten = [0] # Total eaten
        move(mapchars, numRows, numCols, startRow, startCol, sewers, eaten)
        print("\n".join(["".join(col) for col in mapchars]))
        print(f'Total eaten: {eaten[0]}')

    except Exception as E:
        print(E.args[-1])

main()
