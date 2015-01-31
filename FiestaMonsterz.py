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
class FiestaMonsterz():
  ##############################################################################
  def __init__(self):
    ScreenShape = (2200, 1600)
    self.Window = pygame.display.set_mode(ScreenShape)
    pygame.display.set_caption("Window")
    self.MainWorld = World(ScreenShape)
    self.MainWorld.AddEntity(Wall(0, 0, 0, 1600))
    self.MainWorld.AddEntity(Wall(1, 0, 2200, 0))

    self.MainWorld.AddEntity(\
      LoopingFaceRock(self.MainWorld, self.Window, 2200, 1000, -15))

    self.MainWorld.AddEntity(\
      Platform(self.Window, 1100, 1064, 'ZigzagGrass_', 33))

  ##############################################################################
  def AddMonster(self, Id):
    self.MainWorld.AddEntity(JumpMonster(self.Window, 1100, 300), Id)

  ##############################################################################
  def Update(self):
    self.Window.fill(gBlack)
    self.MainWorld.Update()
    pygame.display.flip()

  ##############################################################################
  def AddEvent(self, Id, Event):
    self.MainWorld.AddEventToQueue(Id, Event)

################################################################################
################################################################################
if __name__ == "__main__":
  pygame.init()
  Clock = pygame.time.Clock()
  FiestaMonster = FiestaMonsterz()
  FiestaMonster.AddMonster(0)
  while True:
    for Event in pygame.event.get():
      if (Event.type==pygame.QUIT):
        Quit()
      if Event.type==pygame.KEYDOWN:
        if Event.key == pygame.K_ESCAPE or Event.key == 113:
          Quit()
        elif (Event.key==pygame.K_UP):
          FiestaMonster.AddEvent(0, 'Jump')
    Clock.tick(50)
    FiestaMonster.Update()

