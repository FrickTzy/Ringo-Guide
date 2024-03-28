from Frontend.Interface import WindowEventInterface
import pygame


class LessonWindowEventHandler(WindowEventInterface):
    def __init__(self, window_manager, window, kanji_manager, lesson_window):
        self.__lesson_window = lesson_window
        self.__kanji_manager = kanji_manager
        self.__window = window
        super().__init__(window_manager=window_manager)

    def check_events(self):
        for event in pygame.event.get():
            self.check_if_quit(event=event)
            self.__check_if_key_down(event=event)
        if self.__window.check_if_change_window_size():
            self.__lesson_window.update_size()

    def __check_if_key_down(self, event):
        if not event.type == pygame.KEYDOWN:
            return
        elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            self.__kanji_manager.change_kanji()
