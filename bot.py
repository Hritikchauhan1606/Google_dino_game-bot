from PIL import ImageGrab,ImageOps
import pyautogui,time
from numpy import *
time.sleep(1)
class cord:
    replay=(530,257)
    dino=(231,264)


def restart():
    pyautogui.click(cord.replay)
def space():
    pyautogui.keyDown('space')
    time.sleep(0.01)
    print('jump')
    pyautogui.keyDown('space')


def imagegrab():
    box=(cord.dino[0]+60,cord.dino[1],cord.dino[0]+100,cord.dino[1]+30)
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    print(a.sum())
    return a.sum()
def main():
    restart()
    while True:
        if imagegrab()!=1455:
            space()
            time.sleep(0.1)
main()
