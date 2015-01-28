#!/usr/bin/python

import pygame

from Entities.LoopingFaceRock import LoopingFaceRock
from Entities.JumpMonster import JumpMonster
from World import World

gBlack = (0,0,0)
################################################################################
def Quit():
  pygame.quit()
  exit()

################################################################################
################################################################################
if __name__ == "__main__":
  pygame.init()
  ScreenShape = (2200, 1600)
  Window = pygame.display.set_mode(ScreenShape)
  pygame.display.set_caption("Window")
  Clock = pygame.time.Clock()
  MainWorld = World(ScreenShape)
  MainWorld.AddEntity(LoopingFaceRock(MainWorld, Window, 2200, 1070, -15))
  MainWorld.AddEntity(JumpMonster(Window, 1100, 800))

  while True:
    for Event in pygame.event.get():
      if (Event.type==pygame.QUIT):
        Quit()
      if Event.type==pygame.KEYDOWN:
        if Event.key == pygame.K_ESCAPE or Event.key == 113:
          Quit()
        elif (Event.key==pygame.K_UP):
          print 'might as well jump'
    Window.fill(gBlack)
    MainWorld.Update()
    Clock.tick(50)
    pygame.display.flip()

