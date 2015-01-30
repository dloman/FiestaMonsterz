################################################################################
################################################################################
class ImpactGround(object):
  ##############################################################################
  def __init__(self, InitialState, ImpactFunctor):
    self.State = InitialState
    self.ImpactFunctor = ImpactFunctor

  ###############################################################################
  @property
  def State(self):
    return self.__State

  ###############################################################################
  @State.setter
  def State(self, State):
    if not hasattr(State, 'yVelocity'):
      raise TypeError(str(type(State)) + 'must have yVelocity value')
    self.__State = State

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
  def __call__(self, Rectangle):
    self.State.yVelocity = 0
    self.State.Rectangle.y = Rectangle.y - self.State.Rectangle.height
    self.__ImpactFunctor()

################################################################################
################################################################################


