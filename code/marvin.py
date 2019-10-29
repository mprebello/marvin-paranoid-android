#====================================================================
# Manipule Audio Inputs
# Author: Marcel Rebello
# mail: mprebello@gmail.com
# ====================================================================
from ManipulateAudio import InputAudio
from ManipulateAudio import OutputAudio
from MarvinDrawn import MarvinDrawn
from AnalisysAnswer import AnalisysAnswer
from Action import OpenSoftware
import random
image_marvin = MarvinDrawn()
audio_input = InputAudio(image_marvin)
audio_output = OutputAudio(image_marvin)
audio_output.clean_audio_files()
analisys_message = AnalisysAnswer()

while True:
    image_marvin.silence()
    audio_output.fisrtMessage()
    answer = audio_input.capture()
    analisys_message.verify(answer)
    action = audio_output.message(answer, 'not hide')
    if action != None:
        software_to_manipule = OpenSoftware(action)


