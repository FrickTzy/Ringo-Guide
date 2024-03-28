from pygame import font


class LessonWindowFont:
    __FONT_PATH = "Frontend/Utils/Files/Font/NotoSansJP-Bold.ttf"
    __TEXT_COLOR = (0, 0, 0)
    __TEXT_SIZE_RATIO = 10
    __font: font.Font

    def __init__(self, window_size):
        self.update_font(window_size=window_size)

    def render_text(self, text):
        return self.__font.render(text, True, self.__TEXT_COLOR)

    def update_font(self, window_size):
        window_height = window_size[1]
        self.__font = font.Font(self.__FONT_PATH, self.__font_size(window_height=window_height))

    def __font_size(self, window_height):
        return window_height // self.__TEXT_SIZE_RATIO
