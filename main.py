import pygame
from Backend.Kanji_Saver import KanjiSaver
from Backend.Voice_Pronunciation import VoicePronunciation
from Frontend.Lesson_Window import LessonWindow
from Frontend.Utils.Functions import WindowManager, Window


class Main:
    def __init__(self):
        self.__window_manager = WindowManager()
        self.__window = Window()
        self.__kanji_saver = KanjiSaver()
        self.__voice_pronunciation = VoicePronunciation()
        self.__lesson_window = LessonWindow(window_manager=self.__window_manager, window=self.__window,
                                            kanji_saver=self.__kanji_saver,
                                            voice_pronunciation=self.__voice_pronunciation)

    def run(self):
        while self.__window_manager.running:
            self.__lesson_window.run()
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    Main().run()
