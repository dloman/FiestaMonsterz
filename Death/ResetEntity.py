from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class ResetEntity(object):
  ##############################################################################
  def __init__(self, ResetFunctor, World):
    self.ResetFunctor = ResetFunctor
    self.World = World

  ###############################################################################
  @property
  def ResetFunctor(self):
    return self.__ResetFunctor

  ###############################################################################
  @ResetFunctor.setter
  def ResetFunctor(self, ResetFunctor):
    if not callable(ResetFunctor):
      raise TypeError(str(type(ResetFunctor)) + 'must be callable')
    self.__ResetFunctor = ResetFunctor

  ###############################################################################
  def __call__(self, CollidedObject):
    ResetEntity = self.__ResetFunctor()
    self.World.AddEntity(ResetEntity, None)

################################################################################
################################################################################
