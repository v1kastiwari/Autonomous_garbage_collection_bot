#MainRobot.py
from MotorModule import Motor
from LaneModule import getLaneCurve
import WebcamModule
import cv2 
import ultrasonic as ut
from utlis import initializeTrackbars  # Import the function
##################################################
motor = Motor(32,11,13,33,15,16)
initialTrackBarValues = [87,92,7,220]  # [87,92,7,220]
initializeTrackbars(initialTrackBarValues)

##################################################

def main():
 
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img,1) #1 result , 2 pipeline , 0 none
 
    sen = 1.7  # SENSITIVITY
    maxVAl= 0.2 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    # print(curveVal)
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    # print(curveVal)   
    turn = curveVal*sen 

    # print(turn)
    distance = int(ut.measure_distance())
    if(distance<0):
        distance = 100

    if (distance < 20):
        print(f'ultransonic value{distance}')
        print('stop')
        motor.stop(15)
    else:
        motor.move(0.23,turn,0.05) #(speed,turn,delay)
        print('stearing')
        cv2.waitKey(1)
     
 
if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
        motor.stop(0)  # Stop motors safely
        cv2.destroyAllWindows()  # Close all OpenCV windows
        WebcamModule.cap.release()  # Release webcam