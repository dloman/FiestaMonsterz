from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class Collidable(object):
  ##############################################################################
  def __init__(self, CollisionFunctor, GetPositionFunctor):
    self.CollisionFunctor = CollisionFunctor
    self.GetPositionFunctor = GetPositionFunctor

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
  def GetPositionFunctor(self):
    return self.__GetPositionFunctor

  ##############################################################################
  @GetPositionFunctor.setter
  def GetPositionFunctor(self, GetPositionFunctor):
    if DoesntHaveMethod(GetPositionFunctor, 'GetPosition'):
      raise TypeError(str(type(GetPositionFunctor)) + 'must be callable')
    self.__GetPositionFunctor = GetPositionFunctor

  ##############################################################################
  def Collision(self, CollidedObject):
    self.__CollisionFunctor(CollidedObject, self.GetPosition())

  ##############################################################################
  def GetPosition(self):
    self.__GetPositionFunctor.GetPostion()

################################################################################
################################################################################
