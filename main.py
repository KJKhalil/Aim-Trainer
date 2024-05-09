import math
import random
import time
import pygame
pygame.init()

#Display Window Size And Name
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Aim Trainer')

#Controls The Targets Themselves
class Target:
    MAX_SIZE = 25
    GROWTH_RATE = 0.2
    COLOR = 'red'
    SECOND_COLOR ='white'

    #Makes The Target Appear Then Start Growing
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    #Stops The Target From Continuing To Grow After It Reaches Its Max Size
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    #Creates Multiple Overlapping Circles For That Red/White Target Look
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)

#Allows The Aim Trainer To Run And Allows You To Exit The Window
def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == '__main__':
    main()