import io
import cv2 as cv
import os 
import numpy as np
import mediapipe as mp
import random as rm
import time
import base64
import tkinter
from PIL import Image
# from .__init import *
# from .detector import *
# from .main import *
# from .overlays import *
# from .path import *
# from .reader import *
# from .varb import *

timage = 'Ai/TImage'

MpHand = mp.solutions.mediapipe.python.solutions.hands
hand = MpHand.Hands(max_num_hands=1)
MpDraw = mp.solutions.mediapipe.python.solutions.drawing_utils

Es = 'Ai/Es'