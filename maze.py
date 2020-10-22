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

cols = 20; rows = 20

def makeMap(screen):
    cellMap = []
    for y in range(rows):
        row = []
        for x in range(cols):
            row.append(Cell(x, y, 40, screen))
        cellMap.append(row)
    return cellMap

stack = Stack()

def draw():
    for row in cellMap:
        for element in row:
            element.draw()
            # stack.contains(element.x, element.y)



cellMap = makeMap(screen)

draw()
pygame.display.update()


startCell = cellMap[0][0]
startCell.visited = True
stack.push(startCell)

def generateMaze():
    vistiedCells = 0
    while vistiedCells != cols*rows-1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        if stack.top() == None:
            stack.pop()
            continue

        neighbors = stack.top().getNeighbors(cellMap)

        filteredNeighbors = list(filter(lambda c: c.visited == False, neighbors))

        if len(filteredNeighbors) < 1:
            stack.pop()
            continue
        else:
            randomNr = random.randint(0, len(filteredNeighbors)-1)
            randomNeighbor = filteredNeighbors[randomNr]
            randomNeighbor.visited = True

            stack.push(randomNeighbor)

            vistiedCells += 1


        draw()
        pygame.display.update()


generateMaze()
