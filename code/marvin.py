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
image_marvin = MarvinDrawn()
audio_input = InputAudio(image_marvin)
audio_output = OutputAudio(image_marvin)
analisys_message = AnalisysAnswer()
software_to_manipulate = OpenSoftware()

image_marvin.silence()
marvin_answer = analisys_message.verify('Wake')
audio_output.message('Wake', marvin_answer[1], 'hide')

while True:
    image_marvin.silence()
    human_voice = audio_input.capture()
    marvin_answer = analisys_message.verify(human_voice)
    audio_output.message(human_voice, marvin_answer[1], 'not hide')
#    if marvin_answer[0] != None:
#        software_to_manipulate.task(marvin_answer[0], human_voice)


