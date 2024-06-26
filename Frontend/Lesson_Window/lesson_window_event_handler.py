from Frontend.Interface import WindowEventInterface
from threading import Thread
import pygame


class LessonWindowEventHandler(WindowEventInterface):
    def __init__(self, window_manager, window, kanji_manager, font, background, kanji_saver, voice_pronunciation):
        self.__font = font
        self.__background = background
        self.__kanji_manager = kanji_manager
        self.__window = window
        self.__kanji_saver = kanji_saver
        self.__voice_pronunciation = voice_pronunciation
        super().__init__(window_manager=window_manager)

    def check_events(self):
        for event in pygame.event.get():
            self.__check_if_quit(event=event)
            self.__check_if_key_down(event=event)
            self.__check_if_press_button(event=event)
        if self.__window.check_if_change_window_size():
            self.__update_size()

    def __update_size(self):
        window_size = self.__window.get_size
        self.__font.update_font(window_size=window_size)
        self.__background.update_size(window_size=window_size)

    def __check_if_quit(self, event):
        if not self.check_if_quit(event=event):
            return
        self.__kanji_saver.overwrite_json()
        self.__voice_pronunciation.clear_cache()

    def __check_if_key_down(self, event):
        if not event.type == pygame.KEYDOWN:
            return
        elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            self.__kanji_manager.change_kanji()

    def __check_if_press_button(self, event):
        if not event.type == pygame.MOUSEBUTTONDOWN:
            return
        if not event.button == 1:
            return
        if self.__background.check_if_click_left_corner():
            self.__kanji_saver.append_kanji_dict(kanji_info=self.__kanji_manager.current_kanji)
        elif self.__background.check_if_click_right_corner():
            current_kanji_hiragana = self.__kanji_manager.current_kanji["Reading"]
            Thread(target=self.__voice_pronunciation.play_pronunciation,
                   kwargs={"hiragana_character": current_kanji_hiragana}).start()

