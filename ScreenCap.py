import numpy as np
import cv2 as cv
from PIL import ImageGrab
import os
from discord import File


def get_ss_obj() -> object:
    '''
    Checks for 'disc_screenshots' DIR, creates if it doesn't exist. 
    Takes a screenshot with PIL, converts to numpy array, then swaps color channels BGR->RGB
    Writes screenshot to disc_screenshots DIR, then creates File Obj to be sent via discord.
    '''
    ss = np.array(ImageGrab.grab())
    current = os.path.abspath(os.curdir)
    path_to_screenshots = os.path.join(current, 'discord_screenshots')
    

    if not 'discord_screenshots' in os.listdir():
        os.mkdir(path_to_screenshots)
        
    cv.imwrite(f"{path_to_screenshots}/picture.png", cv.cvtColor(ss, cv.COLOR_BGR2RGB)) 
    
    to_send = File(f"{path_to_screenshots}/picture.png")

    return to_send


if __name__ == "__main__":
    pass
# cv.imwrite('ss.png', cv.cvtColor(ss, cv.COLOR_BGR2RGB)) -> Works, saves image with correct color channels
#current = os.path.abspath(os.curdir) -> #C:\Users\mur81\desktop\vs\z_test
#print(os.listdir()) -> ['bs.py', 'kk', 'main.py']
#FileNotFoundError