import pygame
from .kanji_manager import KanjiManager
from .lesson_window_font import LessonWindowFont
from .lesson_window_pos import LessonWindowPos
from .lesson_window_event_handler import LessonWindowEventHandler
from .lesson_window_background import LessonWindowBackground


class LessonWindow:
    def __init__(self, window_manager, window, kanji_saver, voice_pronunciation):
        pygame.init()
        self.__window = window
        self.__background = LessonWindowBackground(window_size=self.__window.get_size)
        self.__font = LessonWindowFont(window_size=self.__window.get_size)
        self.__kanji_manager = KanjiManager()
        self.__event_handler = LessonWindowEventHandler(window_manager=window_manager, background=self.__background,
                                                        window=window, kanji_manager=self.__kanji_manager,
                                                        font=self.__font, kanji_saver=kanji_saver,
                                                        voice_pronunciation=voice_pronunciation)
        self.__pos = LessonWindowPos(window=self.__window)

    def run(self):
        self.__event_handler.check_events()
        self.__background.show(screen=self.__window.screen)
        self.__blit_text()

    def __blit_text(self):
        current_kanji = self.__kanji_manager.current_kanji
        kanji_surface = self.__font.render_text(text=current_kanji["Kanji"])
        reading_surface = self.__font.render_text(text=current_kanji["Reading"])
        meaning_surface = self.__font.render_text(text=current_kanji["Meaning"])
        kanji_rect = kanji_surface.get_rect(center=(self.__window.width // 2, self.__pos.kanji_y))
        reading_rect = reading_surface.get_rect(center=(self.__window.width // 2, self.__pos.reading_y))
        meaning_rect = meaning_surface.get_rect(center=(self.__window.width // 2, self.__pos.meaning_y))
        self.__window.screen.blit(kanji_surface, kanji_rect)
        self.__window.screen.blit(reading_surface, reading_rect)
        self.__window.screen.blit(meaning_surface, meaning_rect)
