################################################################################
################################################################################
class ImpactGround(object):
  ##############################################################################
  def __init__(self, ImpactFunctor):
    self.ImpactFunctor = ImpactFunctor

  ###############################################################################
  @property
  def ImpactFunctor(self):
    return self.__ImpactFunctor

  ###############################################################################
  @ImpactFunctor.setter
  def ImpactFunctor(self, ImpactFunctor):
    if not callable(ImpactFunctor):
      raise TypeError(str(type(ImpactFunctor)) + 'must be callable')
    self.__ImpactFunctor = ImpactFunctor

  ###############################################################################
  def __call__(self, CollidedObject, State):
    State.yVelocity = 0
    State.Rectangle.y = \
      CollidedObject.GetState().Rectangle.y - State.Rectangle.height
    self.__ImpactFunctor()

################################################################################
################################################################################


