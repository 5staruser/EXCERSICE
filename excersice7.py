from datetime import datetime
from pygame import mixer
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
        break
def logs(msg):
    f=open("msg.txt","a")
    f.write(f"{msg} {datetime.now()}\n")
    f.close
if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_excersice=time()
    watertime=40*60
    eyestime=30*60
    excersicetime=45*60
    while True:
        if time()-init_water>watertime:
            print("water drinking time enter drank to stop alarm")
            musiconloop("water.mp3", "drank")
            init_water=time()
            logs("drank water at")
        if time()-init_eyes>eyestime:
            print("eye excersice time enter doneeye to stop alarm")
            musiconloop("eye.mp3", "doneeye")
            init_eyes=time()
            logs("eyes relaxed at")
        if time()-init_excersice>excersicetime:
            print("physical excersice time enter donephy to stop alarm")
            musiconloop("physical activity.mp3", "donephy")
            init_excersice=time()
            logs("excersice done at")

