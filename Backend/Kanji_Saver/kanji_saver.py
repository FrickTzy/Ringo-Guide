from json import dump, load
from requests import get, put
from threading import Thread


class KanjiSaver:
    __JSON_PATH = "Backend/Saved_Kanji/kanji.json"
    __DB_URL = "https://japanesewords-b38f3-default-rtdb.firebaseio.com/"
    __USE_ONLINE_DB = True

    def __init__(self):
        self.__kanji_list = []
        Thread(target=self.__load_kanji, daemon=True).start()

    def __load_kanji(self) -> None:
        if self.__USE_ONLINE_DB:
            response = get(f'{self.__DB_URL}/user_files/DudeTzy/kanji.json')
            if (saved_json := response.json()) is None:
                kanji_list = []
            else:
                kanji_list = saved_json
        else:
            with open(self.__JSON_PATH, 'r', encoding='utf-8') as json:
                kanji_list = load(json)
        self.__kanji_list = kanji_list

    def append_kanji_dict(self, kanji_info):
        if kanji_info in self.__kanji_list:
            return
        self.__kanji_list.append(kanji_info)

    def save_json(self):
        if self.__USE_ONLINE_DB:
            put(f'{self.__DB_URL}/user_files/DudeTzy/kanji.json', json=self.__kanji_list)
        else:
            with open(self.__JSON_PATH, 'w', encoding='utf-8') as json_file:
                return dump(self.__kanji_list, json_file)
