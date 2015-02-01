import pygame
from random import randint

from Entities.LoopingFaceRock import LoopingFaceRock
from Entities.JumpMonster import JumpMonster
from Entities.Platform import Platform
from Entities.Wall import Wall
from World import World

gBlack = (0,0,0)
################################################################################
################################################################################
class JumpGame():
  ##############################################################################
  def __init__(self):
    ScreenShape = (2200, 1600)
    self.Window = pygame.display.set_mode(ScreenShape)
    pygame.display.set_caption("Window")
    self.MainWorld = World(ScreenShape)
    self.MainWorld.AddEntity(Wall(0, 0, 0, 1600))
    self.MainWorld.AddEntity(Wall(1, 1600, 2200, 0))

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
