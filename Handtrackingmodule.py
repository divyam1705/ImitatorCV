import cv2
import mediapipe as mp
import time

class HandDetector():
    def __init__(self,mode=False,maxhands=2,detectioncon=0.5,trackingcon=0.5):
        self.mode=mode
        self.maxhands=maxhands
        self.detectioncon=detectioncon
        self.trackingcon=trackingcon

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode,self.maxhands,1,self.detectioncon,self.trackingcon)
        self.mpdraw = mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
        #
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgrgb)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpdraw.draw_landmarks(img, handlms, self.mphands.HAND_CONNECTIONS)
        return img
    def findpositon(self,img,draw=True,sid=0):
        handno=0
        lmList=[]
        if self.results.multi_hand_landmarks:
            myhand=self.results.multi_hand_landmarks[handno]
            for id, lm in enumerate(myhand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id,cx,cy])
                if id==sid:
                    cv2.circle(img, (cx, cy), 8, (255, 0, 255), cv2.FILLED)
        return lmList
def main():
    cap = cv2.VideoCapture(0)
    detector=HandDetector()
    while True:
        success, img = cap.read()
        img=detector.findHands(img)
        lmlist=detector.findpositon(img,sid=4)
        cv2.imshow("Image",img)
        cv2.waitKey(1)
if __name__=="__main__"     :
    main()