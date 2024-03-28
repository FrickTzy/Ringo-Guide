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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__window_manager.quit()
