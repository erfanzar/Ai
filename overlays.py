from __init import *


def overlaysimg(self ,img, List ,Num=0  , pos=0):
        
    
    self.self=self
    self.List=List
    self.pos=pos
    self.Num=Num
    ch ,cw ,c = List[Num].shape
    img[pos:ch+pos , pos:cw+pos]=List[Num]



def rects(img , overlays):
        
        
        for overlay in overlays:
        
        
            x , y = overlay.pose
            h , w = overlay.size
            
            cv.rectangle(img,(x,y) , (x+w , h+y) , (0,255,0) )
            cv.rectangle(img,(x,y) , (x+w , h+y) , (0,255,0) )
            
class rec():


    def __init__(self,pose,size,sign):
        
        
        self.pose = pose
        self.size = size
        self.sign =sign            


    def rectangel(self):    
        x , y = self.pose
        h , w = self.size