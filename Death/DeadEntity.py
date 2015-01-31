from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class DeadEntity(object):
  ##############################################################################
  def __init__(self, DeathImage):
    self.GenerateDeadEntityFunctor = GenerateDeadEntityFunctor
    self.World = World

  ###############################################################################
  @property
  def GenerateDeadEntityFunctor(self):
    return self.__GenerateDeadEntityFunctor

  ###############################################################################
  @GenerateDeadEntityFunctor.setter
  def GenerateDeadEntityFunctor(self, GenerateDeadEntityFunctor):
    if not callable(GenerateDeadEntityFunctor):
      raise TypeError(str(type(GenerateDeadEntityFunctor)) + 'must be callable')
    self.__GenerateDeadEntityFunctor = GenerateDeadEntityFunctor

  ###############################################################################
  def __call__(self, DeathState, CollidedObject):
    DeadEntity = self.__GenerateDeadEntityFunctor()
    self.World.AddEntity(DeadEntity)

################################################################################
################################################################################

