from __init import *
from varb import COLORS , NMS_THRESHOLD , CONFIDENCE_THRESHOLD , FONTS

def object_detector(image , model):
    classes, scores, boxes = model.detect(image, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    
    data_list =[]
    for (classid, score, box) in zip(classes, scores, boxes):
        
        color= COLORS[int(classid) % len(COLORS)]
    
        cv.rectangle(image, box, color, 2)
    
        if classid ==0: 
            data_list.append(['person', box[2], (box[0], box[1]-2)])
            
    return data_list



def focal_length_finder (measured_distance, real_width, width_in_rf):
    focal_length = (width_in_rf * measured_distance) / real_width

    return focal_length

def distance_finder(focal_length, real_object_width, width_in_frmae):
    distance = (real_object_width * focal_length) / width_in_frmae
    return distance

def pos(img , rslmhl, handnum = 0 ,):
        lmList= []
        if rslmhl:
            myhand = rslmhl[handnum]
            for id , lm in enumerate(myhand.landmark):
                h,w,c = img.shape
                x ,y = int(lm.x*w) , int(lm.y*h)
                lmList.append([id , x ,y])
               
        return lmList
    
    
    


def pos2 (img , rslmhl):
    
    lllist = []
    if rslmhl:
        myhand = rslmhl[0]
        for id , lm in enumerate(myhand.landmark):
            h ,w,c = img.shape
            x , y = int(lm.x*w) , int(lm.y*h)
            lllist.append([id , x ,y])

    return lllist


