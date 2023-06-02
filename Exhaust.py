# -*- coding: utf-8 -*-

import sys, pygame, math, random
from pygame.locals import *

exhaustLife = 200
exhaustColorOne = (235, 165, 0)
exhaustColorTwo = (200, 125, 100)
ambientPressure = 1
ambientColor = (int(150 * ambientPressure), int(175 * ambientPressure), int(230 * ambientPressure))
exhaustPressure = 1.2
pressureEffectFactor = 1000
exhaustVelocity = 3400
thrust = 50000
nozzleLocationX = 512
nozzleLocationY = 60
nozzleSize = 50

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1024, 720))

while True:
    screen.fill(ambientColor)
    for life in range(exhaustLife):
        for count in range(int(thrust / exhaustVelocity)):
            particleSize = int(34000 / exhaustVelocity / (1 + life / exhaustLife))
            particleX = nozzleLocationX + int(random.randint(-int(nozzleSize / 2 - particleSize), int(nozzleSize / 2 - particleSize))) + int(random.randint(-int(nozzleSize / 2 - particleSize), int(nozzleSize / 2 - particleSize)) * (exhaustPressure * 3/ (ambientPressure + 0.05)) * (1 - (98/100) ** life))
            particleY = nozzleLocationY + int(life * exhaustVelocity / pressureEffectFactor)
            exhaustColorRed = exhaustColorOne[0] - int((exhaustColorOne[0] - (exhaustColorTwo[0] + ambientColor[0]) / 2) * (life / exhaustLife))
            exhaustColorGreen = exhaustColorOne[1] - int((exhaustColorOne[1] - (exhaustColorTwo[1] + ambientColor[1]) / 2) * (life / exhaustLife))
            exhaustColorBlue = exhaustColorOne[2] - int((exhaustColorOne[2] - (exhaustColorTwo[2] + ambientColor[2]) / 2) * (life / exhaustLife))
            pygame.draw.circle(screen, (exhaustColorRed, exhaustColorGreen, exhaustColorBlue), (particleX, particleY), particleSize, 0)
            print(1 - (9/10) ** life)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)





