from abc import ABC, abstractmethod
import pygame


class WindowEventInterface(ABC):
    def __init__(self, window_manager):
        self.__window_manager = window_manager

    @abstractmethod
    def check_events(self):
        pass

    def check_if_quit(self, event):
        if event.type == pygame.QUIT:
            self.__window_manager.quit()
            return True
        if not event.type == pygame.KEYDOWN:
            return False
        if event.key == pygame.K_ESCAPE:
            self.__window_manager.quit()
            return True

