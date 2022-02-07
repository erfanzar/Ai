from operator import index

from detector import *
from overlays import *
from path import LeftArrow ,RightArrow,TopArrow,BottomArrow
from reader import *
from varb import KNOWN_DISTANCE, PERSON_WIDTH ,sign ,size,pose,GREEN,flg,chose,PaddingH,PaddingW,Tip3,Tip2,Tip1, Coructs
from __init import *



def AiNum1(Es ,timage , weights ,cfg ,index):
    StartTest = False
    Coructs = 0
    Wrong = 0
    Wkb=8
    Mkb=15


    BottomSide = cv.imread(f'{Es}/BottomSide.jpg')
    TopSide = cv.imread(f'{Es}/TopSide.jpg')
    LeftSide= cv.imread(f'{Es}/LeftSide.jpg')
    RightSide = cv.imread(f'{Es}/RightSide.jpg')

    ref_person = cv.imread(f'{timage}/image.png')

    BottomSide = cv.resize(BottomSide,(150,150))
    TopSide = cv.resize(TopSide,(150,150))
    LeftSide = cv.resize(LeftSide,(150,150))
    RightSide = cv.resize(RightSide,(150,150))


    vpa = False

    pptime = 0

    ShowStart = False

    yoloNet = cv.dnn.readNet(weights,cfg)
    yoloNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    yoloNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
    model = cv.dnn_DetectionModel(yoloNet)
    
    model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

    def object_detector(image , model):
        classes, scores, boxes = model.detect(image, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
        
        data_list =[]
        for (classid, score, box) in zip(classes, scores, boxes):
            
            color= COLORS[int(classid) % len(COLORS)]
        
            cv.rectangle(image, box, color, 2)
        
            if classid ==0: 
                data_list.append(['person', box[2], (box[0], box[1]-2)])
                
        return data_list



    person_data = object_detector(ref_person,model)
    person_width_in_rf = 200
    focal_person = focal_length_finder(KNOWN_DISTANCE, PERSON_WIDTH, person_width_in_rf)
    lvy=[]
    folderPath = Es
    myList = os.listdir(folderPath)
    for imgpth in myList:
        imgs = cv.imread(f'{folderPath}/{imgpth}')
        lvy.append(imgs)
    minpra = 3 
    maxpra = 10
    cap = cv.VideoCapture(index)
    n , www = cap.read()
    overlays= []
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

        lmList = pos(handnum=0 ,img=img,rslmhl=rslmhl)
        
        
        cv.putText(img, f'fps: {round(fps)}', (20 , 430), FONTS, 0.48, GREEN, 2)
        
        
        # if result.multi_hand_landmarks:
        #     for lm in result.multi_hand_landmarks: 
        #         MpDraw.draw_landmarks(img ,lm ,MpHand.HAND_CONNECTIONS )
        
         ########################       

        data = object_detector(frame,model) 
        llList = pos2(img2,rslmhl=rslmhl)

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
    
        
        
AiNum1(Es=Es , timage=timage ,weights='Ai/yolov4-tiny.weights' , cfg='Ai/yolov4-tiny.cfg',index=0)