from gtts import gTTS
from pygame import mixer
import os

FOLDER_PATH = "Backend/Voice_Pronunciation/Cache/"


class VoicePronunciation:
    __FOLDER_PATH = FOLDER_PATH
    __VOLUME = 1

    def __init__(self):
        self.__pronunciation_fetcher = PronunciationFetcher()
        self.__fetched_pronunciation_sounds = {}

    def play_pronunciation(self, hiragana_character):
        directory_path = f"{self.__FOLDER_PATH}{hiragana_character}.mp3"
        if not os.path.exists(directory_path):
            self.__pronunciation_fetcher.download_hiragana_audio(hiragana_character=hiragana_character)
        if hiragana_character not in self.__fetched_pronunciation_sounds:
            self.__append_fetched_sounds(hiragana_character=hiragana_character, path=directory_path)
        self.__play_sound(hiragana_character=hiragana_character)

    def __append_fetched_sounds(self, hiragana_character, path):
        self.__fetched_pronunciation_sounds[hiragana_character] = mixer.Sound(path)

    def __play_sound(self, hiragana_character):
        mixer.Channel(2).set_volume(self.__VOLUME)
        mixer.Channel(2).stop()
        mixer.Channel(2).play(self.__fetched_pronunciation_sounds[hiragana_character])

    def clear_cache(self):
        self.__pronunciation_fetcher.clear_cache()


class PronunciationFetcher:
    __FOLDER_PATH = FOLDER_PATH

    def __init__(self):
        self.__text_to_speech = gTTS(lang='ja', text="Default")

    def download_hiragana_audio(self, hiragana_character):
        self.__text_to_speech.text = hiragana_character
        self.__text_to_speech.save(f"{self.__FOLDER_PATH}{hiragana_character}.mp3")

    def clear_cache(self):
        cache_files = os.listdir(self.__FOLDER_PATH)
        for file in cache_files:
            os.remove(f"{self.__FOLDER_PATH}{file}")


if __name__ == "__main__":
    hiragana = "みる"
    voice = VoicePronunciation()
