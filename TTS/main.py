from TTS import *
from music import *



#User Input 
#noOfVideo = input("Enter no of videos to be created :") #Disabled for development
noOfVideo = 1

inputTxtFile_array = []
for i in range(int(noOfVideo)):
    #temp_pathtotxtfile = input("Enter Path to File ")   #Disabled for development
    temp_pathtotxtfile = "D:\GIT\TTS\input_text.txt"
    inputTxtFile_array.append(temp_pathtotxtfile)

#OutputPath = input("Enter OutputPath :") #Disabled for development
OutputPath = "D:\GIT\TTS\output"
print("Received File Paths : ", inputTxtFile_array)
#End of User Input 

readTextFile(inputTxtFile_array[0])


# newpath = r'C:\Program Files\arbitrary' 
# if not os.path.exists(newpath):
    # os.makedirs(newpath)

    
# #Read Text File
# inputTxtFile = "D:\GIT\TTS\input_text.txt"

# text_array = []
# with open(inputTxtFile) as my_file:
    # for line in my_file:
        # text_array.append(line)
        # #print(line)

# txtarry_length = len(text_array)
# print("TextFile Length : ",txtarry_length)
#END OF Text File




OutputMP3FilePath = "D:\\GIT\\TTS\\output\\trymusic.mp3"
GetTTSOutput("Hello,    I'm Computer", OutputMP3FilePath, Lang ='en')
Getmusicduration(OutputMP3FilePath)