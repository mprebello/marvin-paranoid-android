#====================================================================
# Manipule Audio Inputs
# Author: Marcel Rebello
# mail: mprebello@gmail.com
# ====================================================================
import speech_recognition as sr
import pyttsx

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
                    self.__image_marvin.blink(2)
                except sr.RequestError as e:
                    self.__image_marvin.blink(3)

class OutputAudio(object):
    def __init__(self, image_marvin):
        self.__audio_directory = 'audio'
        self.__image_marvin = image_marvin
        self.__engine = pyttsx.init()
        rate = self.__engine.getProperty('rate')
        self.__engine.setProperty('rate', rate - 100)

    def message(self, human_voice, marvin_message, status):
        self.__image_marvin.talk()
        if status != 'hide':
            print('Human:{}'.format(human_voice))

        print('Marvin:{}'.format(marvin_message['SentenceToWrite']))
        self.__engine.say(marvin_message['Sentence'])
        self.__engine.runAndWait()


