#WebcamModule.py
import cv2

cap = None  # Don't initialize immediately

def getImg(display=False, size=[480, 240]):
    global cap
    if cap is None:
        cap = cv2.VideoCapture(0)  # Initialize when first called
        # cap = cv2.VideoCapture('vid1.mp4')
        if not cap.isOpened():
            print("Error: Could not open camera")
            return None

    success, img = cap.read()
    if not success:
        print("Warning: Failed to capture image")
        return None
    img = cv2.resize(img, (size[0], size[1]))
    if display:
        cv2.imshow('IMG', img)
        cv2.waitKey(1)
    return img
 
if __name__ == '__main__':
    while True:
        img = getImg(True) # False if you don't want to display the image