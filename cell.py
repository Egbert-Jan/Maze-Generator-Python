import pygame

WHITE = (255, 255, 255)

class Cell:
    visited = False
    size = 20

    def __init__(self, x, y, size, screen):
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        # self.Neighbours = [None, None, None, None]

    def draw(self):
        size = self.size
        x = self.x * size; y = self.y * size
        #left vertical
        pygame.draw.line(self.screen, WHITE, (x, y), (x, y + size))
        # #top horizontal
        pygame.draw.line(self.screen, WHITE, (x, y), (x + size, y))
        # #bottom horizontal
        pygame.draw.line(self.screen, WHITE, (x, y + size), (x + size, y + size))
        # #right vertical
        pygame.draw.line(self.screen, WHITE, (x + size, y), (x + size, y + size))

        if self.visited:
            # print("draw")
            pygame.draw.rect(self.screen, (0, 0, 255) ,(x+3, y+3, size-6, size-6))

    def getNeighbors(self, cellMap):
        x = self.x; y = self.y
        neighbors = []

        if x > 0:
            neighbors.append(cellMap[y][x-1])
        
        if x < len(cellMap)-1:
            neighbors.append(cellMap[y][x+1])

        if y < len(cellMap)-1:
            neighbors.append(cellMap[y+1][x])

        if y > 0:
            neighbors.append(cellMap[y-1][x])

        return neighbors

    def printPosition(self):
        print(self.x, self.y)

    # def __str__(self):
    #     return str(self.x + " " + self.y)
        