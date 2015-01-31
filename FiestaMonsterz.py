#!/usr/bin/python

import pygame

from Entities.LoopingFaceRock import LoopingFaceRock
from Entities.JumpMonster import JumpMonster
from Entities.Platform import Platform
from Entities.Wall import Wall
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
  MainWorld.AddEntity(Wall(0, 0, 0, 1600))
  MainWorld.AddEntity(Wall(1, 0, 2200, 0))
  MainWorld.AddEntity(LoopingFaceRock(MainWorld, Window, 2200, 1000, -15))
  MainWorld.AddEntity(Platform(Window, 1100, 1064, 'ZigzagGrass_', 33))
  MainWorld.AddEntity(JumpMonster(Window, 1100, 300), 0)

  while True:
    for Event in pygame.event.get():
      if (Event.type==pygame.QUIT):
        Quit()
      if Event.type==pygame.KEYDOWN:
        if Event.key == pygame.K_ESCAPE or Event.key == 113:
          Quit()
        elif (Event.key==pygame.K_UP):
          MainWorld.AddEventToQueue(0, 'jump')
    Window.fill(gBlack)
    MainWorld.Update()
    Clock.tick(50)
    pygame.display.flip()

