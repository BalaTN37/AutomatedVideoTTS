from mutagen.mp3 import MP3

def Getmusicduration(InputFilePath):
    audio = MP3(InputFilePath)
    print(audio.info.length)