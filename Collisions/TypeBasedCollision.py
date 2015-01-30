from Utility.Utility import HasMethod
################################################################################
################################################################################
class TypeBasedCollision(object):
  ##############################################################################
  def __init__(self, Killable = None, TypeToActionMap = None):
    self.__TypeToActionMap = {}
    if TypeToActionMap is not None:
      self.__TypeToActionMap = TypeToActionMap
    self.Killable = Killable

  ###############################################################################
  @property
  def Killable(self):
    return self.__Killable

  ###############################################################################
  @Killable.setter
  def Killable(self, Killable):
    if Killable is None or HasMethod(Killable, 'Kill'):
      self.__Killable = Killable
    else:
      raise TypeError(str(type(Killable)) + 'must have Kill method')

  ###############################################################################
  def __call__(self, CollidedObject, Rectangle):
    #TODO make this make more sense
    if CollidedObject:
      if type(CollidedObject) in self.__TypeToActionMap:
        Action = self.__TypeToActionMap[type(CollidedObject)]
        Action(CollidedObject.GetRectangle())
    else:
      if self.__Killable:
        self.__Killable.Kill(CollidedObject)
        print 'outside', (Rectangle.x, Rectangle.y), CollidedObject

################################################################################
################################################################################
