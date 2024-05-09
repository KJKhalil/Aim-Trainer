import math
import random
import time
import pygame
pygame.init()

#Display Window Size And Name
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Aim Trainer')

#Controls The Targets Popping Up And How Quick
TARGET_INCREMENT = 300
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30

BG_COLOR = (0, 25, 40)

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

def draw(win, targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win)

    pygame.display.update()

#Controls How The Aim Trainer Runs
def main():
    run = True

    targets = []

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    #Allows You To Exit The Window
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            #Controls The Random Placement Of Targets And Makes Sure They Appear Within The Window
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

    pygame.quit()

if __name__ == '__main__':
    main()