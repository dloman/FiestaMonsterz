from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class Collidable(object):
  ##############################################################################
  def __init__(self, CollisionFunctor, GetRectangleFunctor):
    self.CollisionFunctor = CollisionFunctor
    self.GetRectangleFunctor = GetRectangleFunctor

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
  def GetRectangleFunctor(self):
    return self.__GetRectangleFunctor

  ##############################################################################
  @GetRectangleFunctor.setter
  def GetRectangleFunctor(self, GetRectangleFunctor):
    if DoesntHaveMethod(GetRectangleFunctor, 'GetRectangle'):
      raise TypeError( \
        str(type(GetRectangleFunctor)) + 'GetRectangle must be defined')
    self.__GetRectangleFunctor = GetRectangleFunctor

  ##############################################################################
  def Collision(self, CollidedObject):
    self.__CollisionFunctor(CollidedObject, self.GetRectangle())

  ##############################################################################
  def GetRectangle(self):
    return self.__GetRectangleFunctor.GetRectangle()

################################################################################
################################################################################
