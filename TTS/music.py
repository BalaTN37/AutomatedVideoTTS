from mutagen.mp3 import MP3
import os
import math

# def Getmusicduration(InputFilePath):
    # audio = MP3(InputFilePath)
    # print(audio.info.length)
    

def mergeMP3toVideo(VideoFilePath, PathtoMP3Files, mp3Length, OutputPath, j ):
    print(PathtoMP3Files)
    tempstring = "ffmpeg -y -i " + VideoFilePath
    for i in range(int(len(PathtoMP3Files))):
        if((PathtoMP3Files[i] != 'None')):
            tempstring = tempstring + " -i "
            tempstring = tempstring + PathtoMP3Files[i]
    tempstring = tempstring + " -filter_complex \""
    
    delayOffset_mp3 = 500 
    notext = 0
    
    for i in range(int(len(PathtoMP3Files))):    
        if((PathtoMP3Files[i] != 'None')):
            tempstring = tempstring + "[" + str(i+1-notext) + "]atrim=0:50,adelay=" #atrim=0:6 -> limit audio to 6 seconds
            tempstring = tempstring + str(delayOffset_mp3) +"|" + str(delayOffset_mp3)
            tempstring = tempstring + "[aud" + str(i+1-notext) + "];"
        else:
            print("Taking else path")
            notext+=1
        whole_second = math.floor(mp3Length[i])
        frac = mp3Length[i] - whole_second      
        frac = frac*100
        whole_mircosecond = math.floor(frac)        
        delayOffset_mp3 = delayOffset_mp3 + (whole_second*1000) + (whole_mircosecond *100)
      
    notext = 0
    
    for i in range(int(len(PathtoMP3Files))):
        if(PathtoMP3Files[i] != "None"):
            tempstring= tempstring + "[aud" + str(i+1-notext) + "]"
        else:
            print("Taking else path")
            notext+=1
            
    tempstring = tempstring + "amix=" + str(len(PathtoMP3Files)+1-notext) + ",apad,atrim=0:50[a]\" -map 0:v -map \"[a]\" -c:v copy -ac 2 "
    tempstring = tempstring + OutputPath + "\output_final_" + str(j) +".mp4"
    
    print(tempstring)
    os.system(tempstring)
    