################################################################################
################################################################################
class Entity(object):
  Counter = 0
  ##############################################################################
  def __init__(self):
    Entity.Counter += 1
    self.Id = Entity.Counter

################################################################################
################################################################################
