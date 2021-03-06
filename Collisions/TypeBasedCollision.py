from Utility.Utility import HasMethod
################################################################################
################################################################################
class TypeBasedCollision(object):
  ##############################################################################
  def __init__(self, DefaultAction = None, TypeToActionMap = None):
    self.__TypeToActionMap = TypeToActionMap or {}
    self.DefaultAction = DefaultAction

  ###############################################################################
  @property
  def DefaultAction(self):
    return self.__DefaultAction

  ###############################################################################
  @DefaultAction.setter
  def DefaultAction(self, DefaultAction):
    if DefaultAction is None or callable(DefaultAction):
      self.__DefaultAction = DefaultAction
    else:
      raise TypeError(str(type(DefaultAction)) + 'must be callable')

  ###############################################################################
  def __call__(self, CollidedObject, State):
    if type(CollidedObject) in self.__TypeToActionMap:
      Action = self.__TypeToActionMap[type(CollidedObject)]
      if callable(Action):
        Action(CollidedObject, State)
    else:
      if self.__DefaultAction:
        self.__DefaultAction(CollidedObject)

################################################################################
################################################################################
