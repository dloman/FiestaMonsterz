################################################################################
def HasMethod(Entity, MethodName):
  return hasattr(Entity, MethodName) and callable(getattr(Entity, MethodName))

################################################################################
def DoesntHaveMethod(Entity, MethodName):
  return \
    not hasattr(Entity, MethodName) or \
    not callable(getattr(Entity, MethodName))
