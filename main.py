import pygame
from numpy import interp
import numpy
from math import cos, sin, atan2, pi

width, height = 1280, 720
window = pygame.display.set_mode((width, height))

k = 10000
fps = pygame.time.Clock()
FPS = 120

def distSquared(a, b, c, d):
    return (a-c)**2 + (b-d)**2

def angleBetween(a, b, c, d):
    return atan2((d - b), (c - a))

class Mark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 5
        self.stretch = 0
        self.angle = 0

    def show_circle(self):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.r)

    def show_line(self):
        #pygame.draw.line(window, (255, 255, 255), (self.x, self.y), (self.x + self.stretch * cos(self.angle), self.y + self.stretch * sin(self.angle)), max(1, int(self.stretch/3)))
        pygame.draw.line(window, (255, 255, 255), (self.x, self.y), (self.x + self.stretch * cos(self.angle), self.y + self.stretch * sin(self.angle)))

class Charge:
    def __init__(self, charge):
        self.q = charge
        self.values = []

    def electricField1(self, mark):
        self.pos = pygame.mouse.get_pos()
        dist = distSquared(self.pos[0], self.pos[1], mark.x, mark.y)
        if dist != 0:
            fieldStrength = k * abs(self.q) / dist
            strength = interp(fieldStrength, [0, 200], [1, 30])
            mark.r = strength
            mark.stretch = strength
            ang = angleBetween(self.pos[0], self.pos[1], mark.x, mark.y)
            if self.q > 0:
                mark.angle = ang
            else:
                mark.angle = pi + ang

    def drawField(self):
        for value in self.values:
            pygame.draw.line(window, (value[0], value[0], value[0]), (value[1], value[2]), (value[1], value[2]))

n = 20
marks = [Mark(width * x //n , height * y //n) for x in range(0, n+1) for y in range(0, n+1)]
electron = Charge(200)
# electron.electricField()

def update():
    window.fill((0, 0, 0))
    for mark in marks:
        mark.show_line()
        electron.electricField1(mark)
    #electron.drawField()
    pygame.display.update()
    fps.tick(FPS)

def loop():
    while True:
        update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

loop()
