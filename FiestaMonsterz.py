#!/usr/bin/python

import pygame

from MainMenu import MainMenu

################################################################################
def Quit():
  pygame.quit()
  exit()

################################################################################
################################################################################
if __name__ == "__main__":
  pygame.init()
  Clock = pygame.time.Clock()
  Menu = MainMenu()
  Game = Menu.GetRandomGame()
  Game.AddMonster(0)
  while True:
    for Event in pygame.event.get():
      if (Event.type==pygame.QUIT):
        Quit()
      if Event.type==pygame.KEYDOWN:
        if Event.key == pygame.K_ESCAPE or Event.key == 113:
          Quit()
        elif (Event.key==pygame.K_UP):
          Game.AddEvent(0, 'Jump')
    Clock.tick(50)
    Game.Update()

