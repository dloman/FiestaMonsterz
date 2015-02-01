#!/usr/bin/python
import sys
from twisted.internet import reactor, protocol
from twisted.internet.task import LoopingCall
from socket import *

from MainMenu import MainMenu

################################################################################
################################################################################
class GameServer(protocol.DatagramProtocol):
  ##############################################################################
  def __init__(self, Game):
    self.Game = Game

  ##############################################################################
  def datagramReceived(self, Datagram, Address):
    if Datagram == "Broadcast Received":
      self.Game.AddMonster(Address[0])
    else:
      self.Game.AddEvent(Address[0], Datagram)

################################################################################
################################################################################
if __name__ == '__main__':
  Game = MainMenu().GetRandomGame()
  GameLoopingCall = LoopingCall(Game.Update)
  GameLoopingCall.start(1/60) #60 fps

  reactor.listenUDP(42069, GameServer(Game))
  reactor.run()
