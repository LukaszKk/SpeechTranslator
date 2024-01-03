import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator


def record_speech(recognizer: sr.Recognizer) -> sr.AudioData:
    with sr.Microphone() as source:
        print("Speak something")
        return recognizer.listen(source)


def speech_to_text(recognizer: sr.Recognizer, audio: sr.AudioData) -> str:
    try:
        print("Understanding language...")
        text = recognizer.recognize_google(audio, language='pl-PL')
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
    return ""


def speech_from_text(text: str) -> gTTS:
    return gTTS(text=text, lang='en')


def translate(translator, text):
    translated = translator.translate(text, src='pl', dest='en')
    return translated.text


def main():
    recognizer = sr.Recognizer()
    translator = Translator()

    audio = record_speech(recognizer)
    text = speech_to_text(recognizer, audio)
    text = translate(translator, text)
    print(text)

    # tts = speech_from_text(text)
    # tts.save("output.mp3")
    # os.system("start output.mp3")


if __name__ == "__main__":
    main()
