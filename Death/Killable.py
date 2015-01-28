from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class Killable(object):
  ##############################################################################
  def __init__(self, KillFunctor):
    self.KillFunctor = KillFunctor
    self.__IsDead = False

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

  ##############################################################################
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
  def Kill(self, CollidedObject):
    self.__IsDead = self.__KillFunctor(CollidedObject)

  ##############################################################################
  def IsDead(self):
    return self.__IsDead

################################################################################
################################################################################
