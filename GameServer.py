#!/usr/bin/python
import sys
from twisted.internet import reactor, protocol
from twisted.internet.task import LoopingCall
from socket import *

from FiestaMonsterz import FiestaMonsterz

################################################################################
################################################################################
class GameServer(protocol.Protocol):
  ##############################################################################
  def connectionMade(self):
    self.factory.Game.AddMonster(self)

  ##############################################################################
  def dataReceived(self, Data):
    self.factory.Game.AddEvent(self, Data)

################################################################################
################################################################################
class GameServerFactory(protocol.ServerFactory):
  ##############################################################################
  def __init__(self, Game):
    self.Game = Game

################################################################################
################################################################################
if __name__ == '__main__':
  FiestaMonster = FiestaMonsterz()
  GameLoopingCall = LoopingCall(FiestaMonster.Update)
  GameLoopingCall.start(1/60) #60 fps

  factory = GameServerFactory(FiestaMonster)
  factory.protocol = GameServer
  reactor.listenTCP(42069, factory)
  reactor.run()
