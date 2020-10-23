from PIL import Image
import pygame
import sys
from stack import Stack
from cell import Cell
import random
import time
import argparse

cols = 20; rows = 20; size = 15
direct = False

(width, height) = (cols*size, rows*size)
screen = pygame.display.set_mode((width+1, height+1))

cellMap = []
stack = Stack()

def createMap():
    tempMap = []
    for y in range(rows):
        row = []
        for x in range(cols):
            row.append(Cell(x, y, size, screen))
        tempMap.append(row)

    return tempMap

def draw():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, rows*size, cols*size))

    for row in cellMap:
        for element in row:
            element.draw()
    
    pygame.display.flip()

def generateMaze():
    vistiedCells = 0

    startCell = cellMap[0][0]
    startCell.visited = True
    stack.push(startCell)

    while vistiedCells != cols*rows-1:

        currentCell = stack.top()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        if currentCell == None:
            stack.pop()
            continue

        neighbors = currentCell.getNeighbors(cellMap)

        filteredNeighbors = list(filter(lambda c: c.visited == False, neighbors))

        if len(filteredNeighbors) < 1:
            stack.pop()
            continue
        else:
            randomNr = random.randint(0, len(filteredNeighbors)-1)
            randomNeighbor = filteredNeighbors[randomNr]
            randomNeighbor.visited = True

            randomNeighbor.connectedNeighbors.append(currentCell)
            currentCell.connectedNeighbors.append(randomNeighbor)
            Cell.currentSelected = currentCell
            stack.push(randomNeighbor)

            vistiedCells += 1

        if direct == False:
            draw()



def main():
    global rows, cols, direct, screen, cellMap

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", type=int, nargs="+")
    parser.add_argument("-d", "--direct", action="store_true")
    args = parser.parse_args()

    if args.size != None:
        rows = args.size[0]
        cols = args.size[1] if len(args.size) >= 2 else cols
    else:
        rows = 40
        cols = 40
    
    direct = args.direct
    (width, height) = (cols*size, rows*size)
    
    screen = pygame.display.set_mode((width+1, height+1))
    pygame.display.set_caption('Maze generator')

    cellMap = createMap()
    generateMaze()
    draw()


if __name__ == "__main__":
    main()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)