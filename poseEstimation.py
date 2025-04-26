import mediapipe as mp
import cv2
import pydirectinput
# Tekken 333ssaaassssaaaaaassssssaaaaassssaaasaaaaaaassssnosa
mpDraw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)
mpPose=mp.solutions.pose
Pose=mpPose.Pose()
punched=False
kicked=False
down=False
def reset_controls():
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("down")
    pydirectinput.keyUp("s")

while True:
    # print("lol")
    success,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Pose.process(imgrgb)
    p20=0
    p12=0
    p19=0
    p11=0
    p0=0
    p10=0

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id , lm in enumerate(results.pose_landmarks.landmark):
            # print(id,lm)
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            if (id == 20):
                p20 =cy
            elif(id==12):
                p12=cy
            elif(id==19):
                p19=cy
            elif(id==11):
                p11=cy
            elif(id==0):
                p0=cy
            elif(id==10):
                p10=cy
            cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
    if (p20<p12 and p19 < p11):
        # print(True)
        # if (down == False):
        down = True
        # reset_controls()
        pydirectinput.keyDown("down")

    else:
        down = False
        pydirectinput.keyUp("down")
    if(down==False and p20<p12):
        # print(True)
        # if(punched==False):
        punched=True
        reset_controls()
        pydirectinput.keyDown("a")

    else:
        punched=False
    if (down==False and p19 < p11):
        # print(True)
        # if (kicked == False):
        kicked = True
        reset_controls()
        pydirectinput.keyDown("s")

    else:
        kicked = False
    pydirectinput.keyUp("a")
    pydirectinput.keyUp("s")
    # pydirectinput.keyUp("down")
    # else:
    #     print(False)wwwwwwwwwwwwwwwwwwwwaaaaaaaaassssaaaaassssasa
    cv2.imshow("Image",img)
    cv2.waitKey(32)
    # 19>11