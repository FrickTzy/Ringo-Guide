class LessonWindowPos:
    __KANJI_Y_RATIO = 3.8
    __READING_Y_RATIO = 2
    __MEANING_Y_RATIO = 1.34

    def __init__(self, window):
        self.__window = window

    @property
    def reading_y(self):
        return self.__window.height // self.__READING_Y_RATIO

    @property
    def kanji_y(self):
        return self.__window.height // self.__KANJI_Y_RATIO

    @property
    def meaning_y(self):
        return self.__window.height // self.__MEANING_Y_RATIO

