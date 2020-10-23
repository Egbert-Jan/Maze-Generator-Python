import pygame

WHITE = (255, 255, 255)

class Cell:
    size = 20
    currentSelected = None

    def __init__(self, x, y, size, screen):
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        self.connectedNeighbors = []
        self.visited = False


    def draw(self):
        size = self.size
        x = self.x * size; y = self.y * size

        if self.visited: #fill
            pygame.draw.rect(self.screen, (0, 0, 0) ,(x, y, size, size))

        if self.currentSelected.x == self.x and self.currentSelected.y == self.y:
            pygame.draw.rect(self.screen, (255, 255, 255) ,(x, y, size, size))

        if self.isConnectedTo(self.x-1, self.y) == False: #left vertical
            pygame.draw.line(self.screen, WHITE, (x, y), (x, y + size))

        if self.isConnectedTo(self.x, self.y-1) == False: # #top horizontal
            pygame.draw.line(self.screen, WHITE, (x, y), (x + size, y))

        if self.isConnectedTo(self.x, self.y+1) == False: # #bottom horizontal
            pygame.draw.line(self.screen, WHITE, (x, y + size), (x + size, y + size))

        if self.isConnectedTo(self.x+1, self.y) == False: # #right vertical
            pygame.draw.line(self.screen, WHITE, (x + size, y), (x + size, y + size))


    def getNeighbors(self, cellMap):
        x = self.x; y = self.y
        neighbors = []

        if x > 0:
            neighbors.append(cellMap[y][x-1])
        
        if x < len(cellMap[0])-1:
            neighbors.append(cellMap[y][x+1])

        if y < len(cellMap)-1:
            neighbors.append(cellMap[y+1][x])

        if y > 0:
            neighbors.append(cellMap[y-1][x])

        return neighbors

    def isConnectedTo(self, x, y):
        for cell in self.connectedNeighbors:
            if cell.x == x and cell.y == y:
                return True
        return False

    def printPosition(self):
        print(self.x, self.y)
        