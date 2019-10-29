#====================================================================
# Manipule Audio Inputs
# Author: Marcel Rebello
# mail: mprebello@gmail.com
# ====================================================================
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import marvin_quotes
import os

class InputAudio(object):
    def __init__(self, image_marvin):
        self.__hotword = 'marvin'
        self.__image_marvin = image_marvin

    def capture(self):
        record = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                audio = record.listen(source)
                try:
                    trigger = record.recognize_google(audio)
                    trigger = trigger.lower()
                    if self.__hotword in trigger:
                        return trigger
                        break
                except sr.UnknownValueError:
                    self.__image_marvin.blink()
                except sr.RequestError as e:
                    self.__image_marvin.blink()

class OutputAudio(object):
    def __init__(self, image_marvin):
        self.__audio_directory = 'audio'
        self.__default_message = marvin_quotes.default
        self.__image_marvin = image_marvin

    def clean_audio_files(self):
        if os.path.exists(self.__audio_directory):
            os.rmdir(self.__audio_directory)

        os.mkdir(self.__audio_directory)
        return None

    def __tts_generate(self, sentence, file, validate=False):
        file_complete = '{}/{}.mp3'.format(self.__audio_directory, file)
        if os.path.isfile(file_complete) != True:
            tts = gTTS(sentence, slow=True, lang='en-uk')
            tts.save(file_complete)

    def __play_sound(self, file):
        playsound('{}/{}.mp3'.format(self.__audio_directory, file))

    def fisrtMessage(self):
        number = random.randint(1, 4)
        self.message('Init-{}'.format(number), 'hide')

    def message(self, answer, status):
        for row in self.__default_message:
            rule = row['Rule']
            sentence = row['Sentence']
            file = row['File']
            action = row['Action']
            if rule in answer:
                self.__tts_generate(sentence, file)
                self.__image_marvin.talk()
                if status != 'hide':
                    print('Human:{}'.format(answer))

                print('Marvin:{}'.format(sentence))
                self.__play_sound(file)
                self.__image_marvin.silence()
                return action
                break;

