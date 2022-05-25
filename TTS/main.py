from TTS import *
from handleSrt import *
from music import *

#User Input 
#noOfVideo = input("Enter no of videos to be created :") #Disabled for development
noOfVideo = 1

inputVideo = "D:\\GIT\\TTS\\box.mp4"

inputTxtFile_array = []
for i in range(int(noOfVideo)):
    #temp_pathtotxtfile = input("Enter Path to File ")   #Disabled for development
    temp_pathtotxtfile = "D:\GIT\TTS\input_text.txt"
    inputTxtFile_array.append(temp_pathtotxtfile)

#OutputPath = input("Enter OutputPath :") #Disabled for development
OutputPath = "D:\GIT\TTS\output"
#print("Received File Paths : ", inputTxtFile_array)
#End of User Input 

for i in range(int(noOfVideo)):
    text_array = readTextFile(inputTxtFile_array[i])
    if not os.path.exists(OutputPath+"\\"+str(i)):
        os.makedirs(OutputPath+"\\"+str(i))
    pathtomp3file, mp3Length = TriggerTTSOut(text_array,OutputPath+"\\"+str(i))
    print("Input Texts", text_array)
    print("Path to mp3 File", pathtomp3file)
    print("mp3 length", mp3Length)

for i in range(int(noOfVideo)):
    createSubtitle(mp3Length, text_array, OutputPath, i)
    mergeSubtitle(inputVideo, OutputPath+"\\Output_"+str(i)+".srt", OutputPath, i)
    mergeMP3toVideo(OutputPath+"\output_"+str(i)+".mp4", pathtomp3file, mp3Length, OutputPath, i)
    #Burn Subtitle






# OutputMP3FilePath = "D:\\GIT\\TTS\\output\\trymusic.mp3"
# GetTTSOutput("Hello,    I'm Computer", OutputMP3FilePath, Lang ='en')
# Getmusicduration(OutputMP3FilePath)