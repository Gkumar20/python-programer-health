from pygame import mixer
from datetime import datetime
import time

class Health:
    "there is using Thread Class Because i want to to program should be run insequence and for relock system"

    def __init__(self,songname):
        self.songname=songname

    def song(self):
        "take song name and play song"
        mixer.init()
        mixer.music.load(f'{self.songname}')
        mixer.music.play()
        time.sleep(10)
        mixer.music.stop()

physical=Health("physical.mp3")
water=Health("water.mp3")
eye = Health("eyes.mp3")

hours=datetime.now().time().hour
minutes=datetime.now().time().minute
sec=datetime.now().time().second

while True:
    if hours >= 9 and hours <= 17:
        if sec<=10:
            mint1,mint2,mint3=26,27,28

            if minutes==mint1:
                physical.song()
                mint1 +=45
                if mint1>=60:
                    mint1=mint1-60
                print("done1")

            if minutes == mint2:
                water.song()
                mint2 += 50
                if mint2 >= 60:
                    mint2 = mint1 - 60
                print("done2")

            if minutes == mint3:
                eye.song()
                mint3 += 30
                if mint3 >= 60:
                    mint3 = mint3 - 60

