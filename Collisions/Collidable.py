from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class Collidable(object):
  ##############################################################################
  def __init__(self, CollisionFunctor, GetStateFunctor):
    self.CollisionFunctor = CollisionFunctor
    self.GetStateFunctor = GetStateFunctor

  ##############################################################################
  @property
  def CollisionFunctor(self):
    return self.__CollisionFunctor

  ##############################################################################
  @CollisionFunctor.setter
  def CollisionFunctor(self, CollisionFunctor):
    if not callable(CollisionFunctor):
      raise TypeError(str(type(CollisionFunctor)) + 'must be callable')
    self.__CollisionFunctor = CollisionFunctor

  ##############################################################################
  @property
  def GetStateFunctor(self):
    return self.__GetStateFunctor

  ##############################################################################
  @GetStateFunctor.setter
  def GetStateFunctor(self, GetStateFunctor):
    if DoesntHaveMethod(GetStateFunctor, 'GetState'):
      raise TypeError(str(type(GetStateFunctor)) + 'GetState must be defined')
    self.__GetStateFunctor = GetStateFunctor

  ##############################################################################
  def Collision(self, CollidedObject):
    self.__CollisionFunctor(CollidedObject, self.GetState())

  ##############################################################################
  def GetState(self):
    return self.__GetStateFunctor.GetState()

################################################################################
################################################################################
