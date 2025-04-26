import mediapipe as mp
import cv2
import pydirectinput
# Tekken 333

mpDraw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)
mpPose=mp.solutions.pose
Pose=mpPose.Pose()
punched=False
kicked=False
down=False
while True:
    success,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Pose.process(imgrgb)
    p20=0
    p12=0
    p19=0
    p11=0
    p0=0
    p10=0
    px20=0
    px19=0
    px14=0
    px13=0
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id , lm in enumerate(results.pose_landmarks.landmark):
            # print(id,lm)wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwass

            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            if (id == 20):
                p20 =cy
                px20=cx
            elif(id==12):
                p12=cy
            elif(id==19):
                p19=cy
                px19=cx
            elif(id==11):
                p11=cy
            elif(id==0):
                p0=cy
            elif(id==10):
                p10=cy
            elif (id == 14):
                px14= cx
            elif (id == 13):
                px13= cx
            cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
    if (px20<px14):
        pydirectinput.keyDown("d")

    else:
        # down = False
        pydirectinput.keyUp("d")
    if (px19>px13):
        pydirectinput.keyDown("a")

    else:
        # down = False
        pydirectinput.keyUp("a")
    if (px20 > px19):
        pydirectinput.keyDown("e")

    else:
        # down = False
        pydirectinput.keyUp("e")
    if(down==False and p20<p12):
        # print(True)wawaaadd
        if(punched==False):
            punched=True
            pydirectinput.keyDown("w")
            # pydirectinput.keyUp("w")
    else:
        punched=False
        pydirectinput.keyUp("w")
    if (down==False and p19 < p11):
        # print(True)
        if (kicked == False):
            kicked = True
            # pydirectinput.keyDown("s")a
            # pydirectinput.keyUp("s")
            pydirectinput.click()
    else:
        kicked = False


    # else:
    #     print(False)wwwwwwwwwwwwwwwwwwww
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    # 19>11