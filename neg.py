# C:/Users/justacold/Desktop/Hackaton/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=training/Positive/
# C:/Users/justacold/Desktop/Hackaton/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec
# C:/Users/justacold/Desktop/Hackaton/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade_out -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 100 -numNeg 70 -numStages 10

from os import listdir

path = "training/Negative/"
with open("neg.txt", "w") as f:
    for file in listdir(path):
        f.write(path + file + '\n')
    
        


