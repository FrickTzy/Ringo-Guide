from pygame import display, RESIZABLE, FULLSCREEN, mouse, cursors
from Frontend.Settings import FULL_SCREEN_VIEW, WINDOW_SIZE


class Window:
    def __init__(self):
        self.__width, self.__height = WINDOW_SIZE
        self.__window = display.set_mode((self.__width, self.__height), RESIZABLE)
        display.set_caption("Japanese Kanji Learning")
        self.__check_full_screen()

    def __check_full_screen(self, full_screen=False):
        if not (FULL_SCREEN_VIEW or full_screen):
            return
        self.__WIDTH, self.__HEIGHT = 1600, 900
        self.__window = display.set_mode((self.width, self.height), FULLSCREEN)
        mouse.set_visible(False)
        mouse.set_cursor(cursors.arrow)

    def check_if_change_window_size(self) -> bool:
        current_width, current_height = self.__window.get_size()
        changed_window_size = current_width != self.width or current_height != self.height
        if changed_window_size:
            self.__width, self.__height = current_width, current_height
            return True
        else:
            return False

    @property
    def screen(self):
        return self.__window

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def get_size(self):
        return self.__width, self.__height