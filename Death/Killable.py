from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class Killable(object):
  ##############################################################################
  def __init__(self, KillFunctor = lambda x: True):
    self.KillFunctor = KillFunctor
    self.IsDead = False

  ###############################################################################
  @property
  def KillFunctor(self):
    return self.__KillFunctor

  ##############################################################################
  @KillFunctor.setter
  def KillFunctor(self, KillFunctor):
    if not callable(KillFunctor):
      raise TypeError(str(type(KillFunctor)) + 'must be callable')
    self.__KillFunctor = KillFunctor

  ##############################################################################
  def Kill(self, CollidedObject):
    self.__KillFunctor(CollidedObject)
    self.IsDead = True

################################################################################
################################################################################
