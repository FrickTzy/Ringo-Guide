from json import dump, load


class KanjiSaver:
    __JSON_PATH = "Backend/Saved_Kanji/kanji.json"

    def __init__(self):
        self.__kanji_list = self.__load_kanji()
        print(self.__kanji_list)

    def __load_kanji(self):
        with open(self.__JSON_PATH, 'r', encoding='utf-8') as json:
            return load(json)["saved_kanji"]

    def append_kanji_dict(self, kanji_info):
        if kanji_info in self.__kanji_list:
            return
        self.__kanji_list.append(kanji_info)

    def overwrite_json(self):
        with open(self.__JSON_PATH, 'w', encoding='utf-8') as json:
            return dump({"saved_kanji": self.__kanji_list}, json)
