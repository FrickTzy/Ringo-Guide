from Backend.Kanji_Fetcher import KanjiFetcher


class KanjiManager:
    __current_kanji = None

    def __init__(self):
        self.__kanji_fetcher = KanjiFetcher()
        self.change_kanji()

    @property
    def current_kanji(self):
        return self.__current_kanji

    def change_kanji(self):
        self.__current_kanji = self.__kanji_fetcher.get_random_kanji()

