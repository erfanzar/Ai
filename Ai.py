
import cv2 as cv
import os 
import numpy as np
import mediapipe as mp
import random as rm
import time

MpHand = mp.solutions.mediapipe.python.solutions.hands
hand = MpHand.Hands(max_num_hands=1)
MpDraw = mp.solutions.mediapipe.python.solutions.drawing_utils



def AiNum1(Es ,timage ,classtxt , weights ,cfg ,index):
    pptime = 0
    Wkb=8
    Mkb=15
    StartTest = False
    ############################

    PaddingW = 500
    PaddingH = 200



    #############################


    BottomSide = cv.imread(f'{Es}/BottomSide.jpg')
    TopSide = cv.imread(f'{Es}/TopSide.jpg')
    LeftSide= cv.imread(f'{Es}/LeftSide.jpg')
    RightSide = cv.imread(f'{Es}/RightSide.jpg')



    BottomSide = cv.resize(BottomSide,(150,150))
    TopSide = cv.resize(TopSide,(150,150))
    LeftSide = cv.resize(LeftSide,(150,150))
    RightSide = cv.resize(RightSide,(150,150))







    #############################


    Tip1 = 100
    Tip2 = 75
    Tip3 = 50
    flg = 600


    ########################

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
            
    Wrong =0

        
    def overlaysimg(self , List ,Num=0  , pos=0):
        
        
        self.self=self
        self.List=List
        self.pos=pos
        self.Num=Num
        ch ,cw ,c = List[Num].shape
        img[pos:ch+pos , pos:cw+pos]=List[Num]



    # def stringToImage(base64_string):
    #     imgdata = base64.b64decode(base64_string)
    #     magePlt = Image.open(io.BytesIO(imgdata))
    #     return magePlt


    # def toRGB(image):
    #    mageRgb = cv.cvtColor(np.array(image), cv.COLOR_BGR2RGB)
    #    return mageRgb


    KNOWN_DISTANCE = 45 #INCHES
    PERSON_WIDTH = 16 #INCHES

    ShowStart = False
    


    CONFIDENCE_THRESHOLD = 0.4
    NMS_THRESHOLD = 0.3


    COLORS = [(255,0,0),(255,0,255),(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
    GREEN =(0,255,0)
    BLACK =(0,0,0)
    FONTS = cv.FONT_HERSHEY_COMPLEX

    ###############################
    Coructs=0
    
    vpa = False
    class_names = []
    


    ##############################


    LeftArrow =  cv.imread(f'{Es}/LeftArrow.jpg',  )
    RightArrow = cv.imread(f'{Es}/RightArrow.jpg', )
    TopArrow =   cv.imread(f'{Es}/TopArrow.jpg',   )
    BottomArrow= cv.imread(f'{Es}/BottomArrow.jpg',)

    LeftArrow   = cv.resize(LeftArrow,  (150,150))
    RightArrow  = cv.resize(RightArrow, (150,150))
    TopArrow    = cv.resize(TopArrow,   (150,150))
    BottomArrow = cv.resize(BottomArrow,(150,150))

    
    # CalLeftArrow = (1-LeftArrow[:,:,3:] / 255) + \
    #     LeftArrow[:,:,:3] * (LeftArrow[:,:,3:] / 255)


    # CalRightArrow = (1-RightArrow[:,:,3:] / 255) + \
    #     RightArrow[:,:,:3] * (RightArrow[:,:,3:] / 255)


    # CalTopArrow = (1-TopSide[:,:,3:] / 255) + \
    #     TopArrow[:,:,:3] * (TopArrow[:,:,3:] / 255)


    # CalBottomArrow = (1-BottomArrow[:,:,3:] / 255) + \
    #     BottomArrow[:,:,:3] * (BottomArrow[:,:,3:] / 255)


    
    
    
    ###############################
    with open(classtxt, "r") as f:
        class_names = [cname.strip() for cname in f.readlines()]
    yoloNet = cv.dnn.readNet(weights,cfg)

    yoloNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    yoloNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)

    model = cv.dnn_DetectionModel(yoloNet)
    model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)


    def object_detector(image):
        classes, scores, boxes = model.detect(image, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
       
        data_list =[]
        for (classid, score, box) in zip(classes, scores, boxes):
           
            color= COLORS[int(classid) % len(COLORS)]
        
            label = "%s : %f" % ('person', score)

            cv.rectangle(image, box, color, 2)
            cv.putText(image, label, (box[0], box[1]-14), FONTS, 0.5, color, 2)
        
            
            if classid ==0: 
                data_list.append(['person', box[2], (box[0], box[1]-2)])
            
        return data_list

    def focal_length_finder (measured_distance, real_width, width_in_rf):
        focal_length = (width_in_rf * measured_distance) / real_width

        return focal_length

    def distance_finder(focal_length, real_object_width, width_in_frmae):
        distance = (real_object_width * focal_length) / width_in_frmae
        return distance
    ref_person = cv.imread(f'{timage}/image1.png')


    person_data = object_detector(ref_person)
    person_width_in_rf = person_data[0][1]

    

    focal_person = focal_length_finder(KNOWN_DISTANCE, PERSON_WIDTH, person_width_in_rf)
    lvy=[]
    folderPath = Es
    myList = os.listdir(folderPath)
    for imgpth in myList:
        imgs = cv.imread(f'{folderPath}/{imgpth}')
        lvy.append(imgs)
    minpra = 3 
    maxpra = 10



    def pos(img , handnum = 0):
        lmList= []
        if rslmhl:
            myhand = rslmhl[handnum]
            for id , lm in enumerate(myhand.landmark):
                h,w,c = img.shape
                x ,y = int(lm.x*w) , int(lm.y*h)
                lmList.append([id , x ,y])
               
        return lmList
    
    
    
    # vvvv=Image.fromarray(numpy_array)



    def pos2 (img):
        
        lllist = []
        if rslmhl:
            myhand = rslmhl[0]
            for id , lm in enumerate(myhand.landmark):
                h ,w,c = img.shape
                x , y = int(lm.x*w) , int(lm.y*h)
                lllist.append([id , x ,y])

        return lllist





    cap = cv.VideoCapture(index)
    n , www = cap.read()
    
    
    overlays= []
    sign = ['Left' , 'Top ' , 'Right ' , 'Bottom']
    pose = [[0,100],[640//2-150,0],[640-160,100],[640//2-150,480-160]]
    size = [[300,160],[160,300],[300,160],[160,300]]

    cap.set(3 , 640)
    cap.set(4 , 480)
    
    
    vvs =1
    for i in range(len(sign)):
            overlays.append(rec(pose[i],size[i],sign[i]))
            
    vvasd = 0
    ptime = 0
    cm = 0
    side = ''

    # if y8>240:
    #             if x8>x4 and y8>y4:
                
    #                 side = 'Bottom'
                
    #         if y8<240:
    #              if x8>x4 and y4>y8:
                
    #                 side = 'Top'   
                
    #         if x8<320:    
    #             if x16>x12>x8 and y16>y12>y8:
                
    #                 side = 'Left'
                    
    #         if x8>320:    
    #             if x16>x12>x8 and y16>y12>y8:
                
    #                 side = 'Right' 



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
    paranoid3 = 600
    
    while True:
        secsu, frame = cap.read()
        frame = cv.flip(frame,1)
        key = cv.waitKey(1)
        imgclr = cv.cvtColor(frame , cv.COLOR_BGR2RGB)
        result = hand.process(imgclr)
        rslmhl = result.multi_hand_landmarks
        img = cv.cvtColor(imgclr ,cv.COLOR_RGB2BGR)
        show = img
        img2 = img
        img2 = cv.resize(img2 , (1270,780))
        show = cv.resize(show,(1270,780))
        cv.rectangle(show,(0,0),(1270,780),(255,255,255),(cv.FILLED))

         ########################       
        
        
        rects(secsu,overlays)

        ctime = time.time()

        fps = 1/(ctime -ptime)
        ptime = ctime

        lmList = pos(handnum=0 ,img=img)
        
        
        cv.putText(img, f'fps: {round(fps)}', (20 , 430), FONTS, 0.48, GREEN, 2)
        
        
        # if result.multi_hand_landmarks:
        #     for lm in result.multi_hand_landmarks: 
        #         MpDraw.draw_landmarks(img ,lm ,MpHand.HAND_CONNECTIONS )
        
         ########################       

        data = object_detector(frame) 
        llList = pos2(img2)

        if len(llList) !=0:
            x8 ,y8 = llList[8][1:]
            
            if vvasd ==0:
                ShowStart = True
                cv.circle(show , (x8,y8),10 , (200,100,150),cv.FILLED)
            if 755<x8<855 and 350<y8<450:
                vvasd = 1
                StartTest = True
                ShowStart = False


        if StartTest ==True and len(lmList) !=0:
            x8,y8 = lmList[8][1:]
            x4,y4 = lmList[4][1:]
            x12,y12 = lmList[12][1:]
            x16,y16 = lmList[16][1:]
            cv.circle(img , (x8,y8) , 10,(0,255,0),cv.FILLED)
        

            if y8>240:
                if x8>x4 and y8>y4:
                
                    side = 'Bottom'
                
            if y8<240:
                 if x8>x4 and y4>y8:
                
                    side = 'Top'   
                
            if x8<320:    
                if x16>x12>x8 and y16>y12>y8:
                
                    side = 'Left'
                    
            if x8>320:    
                if x16>x12>x8 and y16>y12>y8:
                
                    side = 'Right'        

        
         ########################       
        
        
        cv.putText(img , f'{chose[Coructs] } ' , (530,30) , cv.FONT_HERSHEY_PLAIN ,2 ,(255,0,250) , 3) 
        
        
        for d in data:
            if d[0] =='person':
                distance = distance_finder(focal_person, PERSON_WIDTH, d[1])
                x, y = d[2]
            
                kcm = distance * 2.54
                cm = int(kcm)

        paranoid3 = round(np.interp(cm,[150,300] , [500,700]))
        paranoid = np.interp(cm,[150,300] , [Wkb , Mkb])


        Tip1 = round(np.interp(cm,[150,300] , [75,125]))
        Tip2 = round(np.interp(cm,[150,300] , [50,100]))
        Tip2 = round(np.interp(cm,[150,300] , [25,75]) )



        paranoid2 = np.interp(cm,[150,300] ,[500,640])
                
                   
        if StartTest==True and  len(lmList) !=0:
            x8,y8 = lmList[8][1:]
            x4,y4 = lmList[4][1:]
            x12,y12 = lmList[12][1:]
            x16,y16 = lmList[16][1:]
            cv.circle(img , (x8,y8) , 10,(0,255,0),cv.FILLED)
            vpa = True
            
        
            # cv.rectangle(img ,(500 , 420) ,(640 , 480) , GREEN ,2)
            # cv.rectangle(img ,(500 , 420) ,(int(580) , 480) , (255,0,0) ,cv.FILLED)
            # cv.rectangle(img , (0,0) , (150 ,150) , (255,255,255) ,cv.FILLED)
            
            if  side == 'Right':
                hr , wrr ,cr  = RightArrow.shape

                show[flg:flg+hr , flg:flg+wrr] = RightArrow
            
            elif side == 'Left':
                hl , wl ,cl  = LeftArrow.shape

                show[flg:flg+hl , flg:flg+wl] = LeftArrow 
            
            elif side == 'Top':

                ht , yt ,ct  = TopArrow.shape

                show[flg:flg+ht , flg:flg+yt] = TopArrow 


            elif side == 'Bottom':

                hb , yb ,cb  = BottomArrow.shape
            
                show[flg:flg+hb , flg:flg+yb] = BottomArrow 
            
            
            for overlay in overlays:
        
                        
                x ,y =overlay.pose
                h ,w =overlay.size
            
                if x<x8<x+w and y<y8<y+h:
                    
                    if chose[Coructs] == overlay.sign:
                        
                        pptime = 0
                        
                        if vvs ==0:
                        
                            
                            # Coructs +=1
                            Coructs = Coructs + 1
                            
                            vvs = 1
                        if vvs == 1:
                            
                            vvs =0
                        if Coructs ==1:
                            Wkb=15
                            Mkb=18
                        if Coructs<=4:
                            Wkb=10
                        if Coructs>6:
                            Wkb=7
                            Mkb=10
                            
                    else:
                        if pptime == 70:
                            side = ''
                    if chose[Coructs] == side:
                            
                        pptime = 0
                        
                        if vvs ==0:
                        
                            
                            # Coructs +=1
                            Coructs = Coructs + 1
                            vvs = 1
                        if vvs == 1:
                            
                            vvs =0
                        if Coructs ==1:
                            Wkb=15
                            Mkb=18
                        if Coructs<=4:
                            Wkb=10
                        if Coructs>6:
                            Wkb=7
                            Mkb=10
                            
                    else:
                        if pptime == 80:
                            side = ''        
                                
                
                        

                
                #print('Cm :' f'{int(cm)}' ,"|" , "ParanoidOne" , paranoid , "|" , "  ParanoidTwo :" ,paranoid2)
    #       if cm < 50 :
    #          cv.rectangle(img , (15 , 15) ,(400,60) ,BLACK , -1)
    #         cv.putText(img , 'Your Distance isnt Long Enough to keep ' , (25,40) , cv.FONT_HERSHEY_PLAIN ,1 , (255,0,0),2)
        #    else :
        #       cv.rectangle(img , (15 , 15) ,(400,60) ,GREEN , -1)
        #       cv.putText(img , 'Your Distance Is fine If Your Ready Press G ' , (25,40),  cv.FONT_HERSHEY_PLAIN ,1 , (255,0,0) ,2)
                
                
                cv.putText(show, f'Distance : {round(cm)} Cm', (800,300), cv.FONT_ITALIC,  1, GREEN, 2)
                
                if cm >250 :
                   
                    cv.putText(show , 'please stay closer to camera ' , (25,500) , cv.FONT_ITALIC ,1 , (255,0,0) , thickness=2)

               
                        
                        
                        
                # print(f'Time : {pptime}  //  Wrongs : {Wrong}')                        
                        
                        
                        
                # if key == ord('t'):
                #     if cm < 50 :
                #         cv.rectangle(img , (15 , 80) ,(400,60) ,BLACK , -1)
                #         cv.putText(img , 'Your Distance isnt Long Enough to keep ' , (25,320) , cv.FONT_HERSHEY_PLAIN ,3 , (255,0,0))
                #     else : 
                #         cv.rectangle(img , (15 , 80) ,(400,60) ,BLACK , -1)
                #         cv.putText(img , 'Close Your Left Eye' , (25,320) , cv.FONT_HERSHEY_PLAIN ,3 , (255,0,0))
                        
                        
                        
                        
                        
                        
                        
                        
                        
               ################################# Das Nazan Bache #####################         
        # ret , buffer =  cv.imencode('.jpg' , img)
        # frame = buffer.tobytes()
        # yield(b'--frame\r\n'
        #         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
   
        if vpa == True:
            print(pptime)
            pptime +=1
            if pptime == 30:
                Wrong +=1
                pptime = 0


        img = cv.resize(img ,(300,200))
        hhs , wws ,ccs = img.shape    
        vh = 580
        vw = 970
        # chart = cv.imread(f'{Es}/EyeChartNIgga.jpg')
        # chart = cv.resize(chart,(paranoid3,paranoid3))
        # hhg , wwg ,ccg = chart.shape
        vvh =10
        vvw =100
        # show[vvh:vvh+hhg , vvw:vvw+wwg]= chart
        # if y8>240:
        #         if x8>x4 and y8>y4:
                
        #             side = 'Bottom'
                
        #     if y8<240:
        #          if x8>x4 and y4>y8:
                
        #             side = 'Top'   
                
        #     if x8<320:    
        #         if x16>x12>x8 and y16>y12>y8:
                
        #             side = 'Left'
                    
        #     if x8>320:    
        #         if x16>x12>x8 and y16>y12>y8:
                
        #             side = 'Right' 
        if StartTest ==True:
            if chose[Coructs] == 'Left':

                if Coructs >= 3:
                    LeftSide = cv.resize(LeftSide , (Tip1,Tip1))

                if Coructs >= 8:
                    LeftSide = cv.resize(LeftSide , (Tip2,Tip2))
                if Coructs >= 15:
                    LeftSide = cv.resize(LeftSide , (Tip3,Tip3))
                        


                hl , wl ,cl =LeftSide.shape
                show[PaddingH:PaddingH+hl ,PaddingW:PaddingW+wl] = LeftSide

            elif chose[Coructs] == 'Right':
                if Coructs >= 3:
                    RightSide = cv.resize(RightSide , (Tip1,Tip1))

                if Coructs >= 8:
                     RightSide = cv.resize(RightSide , (Tip2,Tip2))
                if Coructs >= 16:
                    RightSide = cv.resize(RightSide , (Tip3,Tip3))     
                hr , wr ,cr =RightSide.shape

                show[PaddingH:PaddingH+hr ,PaddingW:PaddingW+wr] = RightSide  


            elif chose[Coructs] == 'Top':
                if Coructs >= 3:
                    TopSide = cv.resize(TopSide , (Tip1,Tip1))
                
                if Coructs >= 8:
                    TopSide = cv.resize(TopSide , (Tip2,Tip2))

                if Coructs >= 15:
                    TopSide = cv.resize(TopSide , (Tip3,Tip3))


                ht , wt ,ct =TopSide.shape
                show[PaddingH:PaddingH+ht ,PaddingW:PaddingW+wt] = TopSide 


            elif chose[Coructs] == 'Bottom':
                if Coructs >= 3:
                    BottomSide = cv.resize(BottomSide , (Tip1,Tip1))
                if Coructs >= 8:
                    BottomSide = cv.resize(BottomSide , (Tip2,Tip2))
                if Coructs >= 15:
                    BottomSide = cv.resize(BottomSide , (Tip3,Tip3))
                        
                        
                hb , wb ,cb =BottomSide.shape
                show[PaddingH:PaddingH+hb ,PaddingW:PaddingW+wb] = BottomSide 

        show[vh:vh+hhs , vw:vw+wws]= img

        if ShowStart == True:
            cv.circle(show,(800,400),80,(255,255,0),cv.FILLED)    
            cv.putText(show,('Start'),(760,410),cv.FONT_ITALIC , 1 , (0,0,0),2)  
            


        cv.putText(show,f'Coructs:{Coructs} / Wrongs : {Wrong}' , (800 , 80) , cv.FONT_ITALIC , 1,(255,255,0),2)

        cv.putText(show,f'{chose[Coructs]}' , (800 , 150) , cv.FONT_ITALIC , 1,(255,255,0),2)

        if Wrong >= 3:
            cv.putText(show , 'You Lost ' ,(300,750) , cv.FONT_ITALIC , 1 , (255,250,0) ,3)


        cv.imshow('Ai',show)

        
        
        if cv.waitKey(1)==ord('q'):
            break
    
        
        
AiNum1( 'Es',
        'TImage',
        'classes.txt',
        'yolov4-tiny.weights',
        'yolov4-tiny.cfg',
        0)
##C:/Users/REZA/Desktop/Erfun/Flask/