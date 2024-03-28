import pygame
from Frontend.Lesson_Window import LessonWindow
from Frontend.Utils.Functions import WindowManager, Window


class Main:
    def __init__(self):
        self.__window_manager = WindowManager()
        self.__window = Window()
        self.__lesson_window = LessonWindow(window_manager=self.__window_manager, window=self.__window)

    def run(self):
        while self.__window_manager.running:
            self.__lesson_window.run()
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    Main().run()
