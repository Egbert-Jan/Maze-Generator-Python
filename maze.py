from PIL import Image
import pygame
import sys
from stack import Stack
from cell import Cell
import random
import time

(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Maze generator')

cols = 9; rows = 9

cellMap = []
stack = Stack()

for y in range(rows):
    row = []
    for x in range(cols):
        row.append(Cell(x, y, 40, screen))
    cellMap.append(row)

def draw():
    for row in cellMap:
        for element in row:
            element.draw()

startCell = cellMap[0][0]
startCell.visited = True
stack.push(startCell)



def generateMaze():
    vistiedCells = 0
    while vistiedCells != cols*rows-1:

        currentCell = stack.top()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

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

            stack.push(randomNeighbor)

            vistiedCells += 1

        pygame.draw.rect(screen, (0, 0, 0), (0, 0, rows*40, cols*40))
        draw()
        pygame.display.flip()


generateMaze()

for row in cellMap:
    for element in row:
        print(element.x, element.y, len(element.connectedNeighbors))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()