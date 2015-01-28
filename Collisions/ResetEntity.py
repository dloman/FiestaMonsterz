from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class ResetEntity(object):
  ##############################################################################
  def __init__(self, ResetFunctor, Killable, World):
    self.ResetFunctor = ResetFunctor
    self.Killable = Killable
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
  @property
  def Killable(self):
    return self.__Killable

  ###############################################################################
  @Killable.setter
  def Killable(self, Killable):
    if DoesntHaveMethod(Killable, 'Kill'):
      raise TypeError(str(type(Killable)) + 'must have Kill method')
    self.__Killable = Killable

  ###############################################################################
  def __call__(self, CollidedObject, Position):
    #TODO make this make more sense
    if not CollidedObject:
      self.__Killable.Kill(CollidedObject)
      ResetEntity = self.__ResetFunctor()
      self.World.AddEntity(ResetEntity)
    else:
      print 'this shouldnt be here', Position, CollidedObject

################################################################################
################################################################################

