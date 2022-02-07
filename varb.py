from __init import *


pptime = 0

Wrong = 0

PaddingW = 500
PaddingH = 200


chose = [
        'Right',
        'Left',
        'Top',
        'Right',
        'Bottom',
        'Bottom',
        'Left',
        'Top',
        'Right',
        'Left',
        'Top',
        'Right', 
        'Bottom',
        'Left',
        'Top',
        'Right',
        'Bottom',
        'Left',
        'Top',
        'Right',
        'Bottom',
        'Left',
        'Top',
        'Right',
        'Bottom'
    ]



Tip1 = 100
Tip2 = 75
Tip3 = 50
flg = 600

sign = ['Left' , 'Top ' , 'Right ' , 'Bottom']
pose = [[0,100],[640//2-150,0],[640-160,100],[640//2-150,480-160]]
size = [[300,160],[160,300],[300,160],[160,300]]


Wrong =0

        


KNOWN_DISTANCE = 45 
PERSON_WIDTH = 16 

ShowStart = False



CONFIDENCE_THRESHOLD = 0.4
NMS_THRESHOLD = 0.3


COLORS = [(255,0,0),(255,0,255),(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
GREEN =(0,255,0)
BLACK =(0,0,0)
FONTS = cv.FONT_HERSHEY_COMPLEX

Coructs=0

vpa = False
class_names = []
