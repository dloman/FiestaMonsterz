#!/usr/bin/python

import copy
from itertools import combinations

from Utility.Utility import HasMethod

################################################################################
################################################################################
class World(object):
  ##############################################################################
  def __init__(self, ScreenShape):
    self.ScreenWidth, self.ScreenHeight = ScreenShape
    self.__IdToEntityMap = {}
    self.__Collidable = []
    self.__Movable = []
    self.__Drawable = []
    self.__Killable = []
    self.__EventList = []

  ##############################################################################
  @property
  def ScreenWidth(self):
    return self.__ScreenWidth

  ##############################################################################
  @ScreenWidth.setter
  def ScreenWidth(self, ScreenWidth):
    if ScreenWidth < 0:
      raise ValueError("Screen Width must be positive")
    self.__ScreenWidth = ScreenWidth

  ##############################################################################
  @property
  def ScreenHeight(self):
    return self.__ScreenHeight

  ##############################################################################
  @ScreenHeight.setter
  def ScreenHeight(self, ScreenHeight):
    if ScreenHeight < 0:
      raise ValueError("Screen Width must be positive")
    self.__ScreenHeight = ScreenHeight

  ##############################################################################
  def AddEntity(self, Entity, Id = None):
    if HasMethod(Entity, 'Collision') and HasMethod(Entity, 'GetRectangle'):
      self.__Collidable.append(Entity)

    if HasMethod(Entity, 'Move'):
      self.__Movable.append(Entity)

    if HasMethod(Entity, 'IsDead'):
      self.__Killable.append(Entity)

    if HasMethod(Entity, 'Draw'):
      self.__Drawable.append(Entity)

    if \
     HasMethod(Entity, 'ProcessEvents') and \
     HasMethod(Entity, 'AddEventToQueue'):
      self.__EventList.append(Entity)
      self.__IdToEntityMap[Id] = Entity

  ##############################################################################
  def Update(self):
    for Entity in self.__EventList:
      Entity.ProcessEvents()

    self.CheckForCollisions()

    self.RemoveKilledEntities()

    for Entity in self.__Drawable:
      Entity.Draw()

    for Entity in self.__Movable:
      Entity.Move()

  ##############################################################################
  def CheckForCollisions(self):
    CollidableObjects = copy.copy(self.__Collidable)
    for Lhs, Rhs in combinations(CollidableObjects, 2):
      if Lhs.GetRectangle().colliderect(Rhs.GetRectangle()):
        Lhs.Collision(Rhs)
        Rhs.Collision(Lhs)
    for Entity in CollidableObjects:
      xPosition, yPosition = Entity.GetPosition()
      if not self.OnScreen(xPosition, yPosition):
        Entity.Collision(None)

  ##############################################################################
  def OnScreen(self, xPosition, yPosition):
    return \
      0 < xPosition <= self.__ScreenWidth and \
      0 < yPosition <= self.__ScreenHeight

  ##############################################################################
  def RemoveKilledEntities(self):
    KilledEntities = []
    for Entity in self.__Killable:
      if Entity.IsDead():
        KilledEntities.append(Entity)

    for KilledEntity in KilledEntities:
      if KilledEntity in self.__Killable:
        self.__Killable.remove(KilledEntity)

      if KilledEntity in self.__Drawable:
        self.__Drawable.remove(KilledEntity)

      if KilledEntity in self.__Collidable:
        self.__Collidable.remove(KilledEntity)

      if KilledEntity in self.__Movable:
        self.__Movable.remove(KilledEntity)

      self.__IdToEntityMap = \
        {Key: Value for Key, Value in self.__IdToEntityMap.items() \
          if Value is not KilledEntity}

  ##############################################################################
  def AddEventToQueue(self, Id, Event):
    Entity = self.__IdToEntityMap[Id]
    if Entity in self.__EventList:
      Entity.AddEventToQueue(Event)


################################################################################
################################################################################
