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
    if HasMethod(Entity, 'Collision') and HasMethod(Entity, 'GetState'):
      self.__Collidable.append(Entity)

    if HasMethod(Entity, 'Move'):
      self.__Movable.append(Entity)

    if HasMethod(Entity, 'Kill') and hasattr(Entity, 'IsDead'):
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
    self.CheckForCollisions()

    self.RemoveKilledEntities()

    for Entity in self.__EventList:
      Entity.ProcessEvents()

    for Entity in self.__Drawable:
      Entity.Draw()

    for Entity in self.__Movable:
      Entity.Move()

  ##############################################################################
  def CheckForCollisions(self):
    CollidableObjects = copy.copy(self.__Collidable)
    for Lhs, Rhs in combinations(CollidableObjects, 2):
      if Lhs.GetState().Rectangle.colliderect(Rhs.GetState().Rectangle):
        Lhs.Collision(Rhs)
        Rhs.Collision(Lhs)

  ##############################################################################
  def OnScreen(self, xPosition, yPosition):
    return \
      0 < xPosition <= self.__ScreenWidth and \
      0 < yPosition <= self.__ScreenHeight

  ##############################################################################
  def RemoveKilledEntities(self):
    KilledEntities = []
    for Entity in self.__Killable:
      if Entity.IsDead:
        KilledEntities.append(Entity)

    for KilledEntity in KilledEntities:
      self.RemoveEntity(KilledEntity)

  ##############################################################################
  def RemoveEntity(self, Entity):
      if Entity in self.__Killable:
        self.__Killable.remove(Entity)

      if Entity in self.__Drawable:
        self.__Drawable.remove(Entity)

      if Entity in self.__Collidable:
        self.__Collidable.remove(Entity)

      if Entity in self.__Movable:
        self.__Movable.remove(Entity)

      self.__IdToEntityMap = \
        {Key: Value for Key, Value in self.__IdToEntityMap.items() \
          if Value is not Entity}

  ##############################################################################
  def AddEventToQueue(self, Id, Event):
    if Id in self.__IdToEntityMap:
      Entity = self.__IdToEntityMap[Id]
      if Entity in self.__EventList:
        Entity.AddEventToQueue(Event)

################################################################################
################################################################################
