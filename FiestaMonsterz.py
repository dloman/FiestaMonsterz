#!/usr/bin/python

import pygame

from Entities.LoopingFaceRock import LoopingFaceRock
from Entities.JumpMonster import JumpMonster
from Entities.Platform import Platform
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
  MainWorld.AddEntity(1, LoopingFaceRock(MainWorld, Window, 2200, 1000, -15))
  MainWorld.AddEntity(2, JumpMonster(Window, 1100, 800))
  MainWorld.AddEntity(3, Platform(Window, 1100, 1064, 'ZigzagGrass_', 33))

  while True:
    for Event in pygame.event.get():
      if (Event.type==pygame.QUIT):
        Quit()
      if Event.type==pygame.KEYDOWN:
        if Event.key == pygame.K_ESCAPE or Event.key == 113:
          Quit()
        elif (Event.key==pygame.K_UP):
          MainWorld.AddEventToQueue(2, 'jump')
    Window.fill(gBlack)
    MainWorld.Update()
    Clock.tick(50)
    pygame.display.flip()

