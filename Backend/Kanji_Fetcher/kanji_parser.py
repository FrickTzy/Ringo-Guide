import csv
from openai import OpenAI
from json import loads, load
from time import sleep


class KanjiParser:
    __PATH = 'Kanji_Files/n1.csv'
    __NEW_PATH = 'Kanji_Files/n1.csv'
    __DEFAULT_VALUE = "None"

    def __init__(self):
        self.__client = OpenAI(api_key="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")
        self.__kanji_original_info_list = []
        self.__kanji_new_info_list = []

    def add_examples_to_csv(self):
        self.__read_csv()
        self.__fetch_info_list()
        self.__overwrite_csv()

    def __read_csv(self):
        with open(self.__PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            self.__kanji_original_info_list = list(reader)

    def __read_example_csv(self):
        with open(self.__NEW_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            self.__kanji_original_info_list = list(reader)

    def __overwrite_csv(self):
        with open(self.__NEW_PATH, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Kanji', 'Reading', 'Meaning', "Japanese Example", "English Example"])
            for kanji_info in self.__kanji_new_info_list:
                writer.writerow(kanji_info)

    def __fetch_info_list(self):
        starting_index, ending_index = 0, 40
        while len(self.__kanji_new_info_list) < (goal_len := len(self.__kanji_original_info_list)):
            if ending_index > goal_len:
                ending_index = goal_len
            current_kanji_list = self.__kanji_original_info_list[starting_index: ending_index]
            try:
                fetched_dict = self.__fetch_examples(kanji_list=current_kanji_list)
            except IndexError:
                current_kanji_list = self.__kanji_original_info_list[starting_index: ending_index]
                fetched_dict = self.__fetch_examples(kanji_list=current_kanji_list)
            for index in range(starting_index, ending_index):
                current_list = self.__kanji_original_info_list[index]
                kanji, reading, meaning = current_list["Kanji"], current_list["Reading"], current_list["Meaning"]
                if kanji in fetched_dict:
                    japanese_example = fetched_dict[kanji]["Japanese"]
                    english_example = fetched_dict[kanji]["English"]
                else:
                    japanese_example, english_example = self.__DEFAULT_VALUE, self.__DEFAULT_VALUE
                new_kanji_info_list = [kanji, reading, meaning, japanese_example, english_example]
                print(new_kanji_info_list, index, goal_len)
                self.__kanji_new_info_list.append(new_kanji_info_list)
            starting_index += 40
            ending_index += 40
            sleep(5)

    def overwrite_csv_with_list(self, csv_list):
        self.__read_csv()
        self.__override_list(csv_list=csv_list)
        self.__overwrite_csv()

    def __override_list(self, csv_list):
        for kanji_info in csv_list:
            self.__kanji_new_info_list.append(kanji_info)
        for kanji_info in self.__kanji_original_info_list:
            kanji, reading, meaning = kanji_info["Kanji"], kanji_info["Reading"], kanji_info["Meaning"]
            japanese_example, english_example = kanji_info["Japanese Example"], kanji_info["English Example"]
            new_kanji_info_list = [kanji, reading, meaning, japanese_example, english_example]
            self.__kanji_new_info_list.append(new_kanji_info_list)

    def get_info_dict(self):
        self.__read_csv()
        with open("Kanji_Files/Test/add.json", "r", encoding="utf-8") as json:
            fetched_dict = load(json)
        for index in range(41):
            current_list = self.__kanji_original_info_list[index]
            kanji, reading, meaning = current_list["Kanji"], current_list["Reading"], current_list["Meaning"]
            if kanji in fetched_dict:
                japanese_example = fetched_dict[kanji]["Japanese"]
                english_example = fetched_dict[kanji]["English"]
            else:
                japanese_example, english_example = self.__DEFAULT_VALUE, self.__DEFAULT_VALUE
            new_kanji_info_list = [kanji, reading, meaning, japanese_example, english_example]
            print(new_kanji_info_list)

    def __fetch_examples(self, kanji_list):
        completion = self.__client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a kanji example ai, generating examples from a kanji input."},
                {"role": "user",
                 "content": f"Give me one sentence example for each of these kanji in the list: {kanji_list}, "
                            "with the english and japanese translation, give it to me in json form. Example:"
                            "Input is 青, it will output: {'青': {'Japanese': '今日は空が青い。', "
                            "'English': 'The sky is blue today.'}"}

            ]
        )
        return loads(completion.choices[0].message.content)


def main():
    parser = KanjiParser()
    parser.add_examples_to_csv()


if __name__ == "__main__":
    main()
