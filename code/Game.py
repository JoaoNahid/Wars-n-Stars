from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Level import Level
from code.Menu import Menu

import pygame

from code.Score import Score
from code.Tutorial import Tutorial


class Game:

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512) # init mixer
        pygame.init()
        pygame.mixer.set_num_channels(16)
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.action = None

    def run(self):
        while True:
            menu = Menu(self.window)
            self.action = menu.run()

            match self.action.lower():
                case 'new game 1p':
                    level = Level(self.window, 'Level 1', '1P')
                    level.run()
                case 'new game 2p':
                    level = Level(self.window, 'Level 1', '2P')
                    level.run()
                case 'tutorial':
                    tutorial = Tutorial(self.window)
                    tutorial.run()
                case 'score':
                    score = Score(self.window)
                    score.run()
                case 'exit':
                    self.quit()
                case _:
                    pass


    @staticmethod
    def quit():
        pygame.quit()  # Close window
        quit()  # End pygame


