from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io
import os
import tempfile


def play_hiragana_audio(hiragana_character):
    tts = gTTS(text=hiragana_character, lang='ja')

    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    audio_segment = AudioSegment.from_file(audio_stream, format="mp3")

    play(audio_segment)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp_dir:
        os.environ["TMP"] = tmp_dir
        play_hiragana_audio("めいめい")