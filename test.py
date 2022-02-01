import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

Net = cv.dnn.readNet('Yolov4-Custom.weights' ,'yolov4s-tiny.cfg')
# frame = cv.imread('download.jpg')


Net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
Net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

model = cv.dnn_DetectionModel(Net)

model.setInputParams(size=(416,416) , scale=1/255 , swapRB=True)



Labels = [
    'Bottom',
    'Left',
    'Right',
    'Top'
]



while True:


    grab , frame  = cam.read()

    frame = cv.resize(frame,(1270,780))

    classes , scores , bboxs = model.detect(frame)

    for (classid , score , bbox ) in zip(classes ,scores , bboxs):

        Name = Labels[classid[0]]
        Accuracy = score[0]
        print(Name , score)

        cv.rectangle(frame , (bbox[0], bbox[1]) , (bbox[0]+bbox[2] , bbox[1]+bbox[3]) , (255,255,0) , 2)     

        cv.rectangle(frame , (bbox[0], bbox[1]-50) , (bbox[0]+500 , bbox[1]) , (255,255,0) , cv.FILLED)

        cv.putText(frame , f'{Name} :  {Accuracy}' , (bbox[0]+5 , bbox[1]-10) , cv.FONT_ITALIC , 1 , (0,0,0) , 3) 



    cv.imshow('detect' , frame)
    cv.waitKey(1)

    if cv.waitKey(1) == ord('q'):
        break