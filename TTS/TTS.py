# Import the required module for text 
# to speech conversion
from gtts import gTTS
# This module is imported so that we can 
# play the converted audio
import os


def readTextFile(InputFilePath):
    text_array = []
    with open(InputFilePath) as my_file:
        for line in my_file:
            text_array.append(line)
            #print(line)
    txtarry_length = len(text_array)
    #print("TextFile Length : ",txtarry_length)


def GetTTSOutput(InputText, OutputFilePath, Lang ='en'):
    # The text that you want to convert to audio
    # mytext = 'Hello I'm Computer'
    mytext = InputText
      
    # Language in which you want to convert
    language = Lang
      
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
      
    # Saving the converted audio in a mp3 file named
    # welcome 
    # myobj.save("welcome.mp3")
    myobj.save(OutputFilePath)
      
    # Playing the converted file
    # os.system("mpg321 welcome.mp3")