import csv
import os
from random import randint, choice


class KanjiFetcher:
    __PATH_FOLDER = "Backend\Kanji_Fetcher\Kanji_Files"
    __KANJI_RANGE = 5

    def __init__(self):
        self.__fetched_kanji_dict = {}

    def get_random_kanji(self):
        kanji_path = self.__get_random_kanji_path
        if kanji_path in self.__fetched_kanji_dict:
            return choice(self.__fetched_kanji_dict[kanji_path])
        with open(kanji_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            kanji_info_list = list(reader)
            self.__fetched_kanji_dict[kanji_path] = kanji_info_list
            return choice(kanji_info_list)

    @property
    def __get_random_kanji_path(self):
        chosen_kanji_csv = randint(1, 5)
        return os.path.join(self.__PATH_FOLDER, f"n{chosen_kanji_csv}.csv")


def main():
    fetcher = KanjiFetcher()
    print(fetcher.get_random_kanji())


if __name__ == "__main__":
    main()
