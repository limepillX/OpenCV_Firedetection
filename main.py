import os, winsound, time
import uuid
import colortext
import cv2

#TODO
# - new training model
# - UI?
# - Smoke detection
# - TG bot?

def display_info(img, times):
    cv2.putText(img,f'{FRAMERATE=}', (0, 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,255),2 ,2)
    cv2.putText(img,f'{SENSITIVITY=}', (0, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,255),2 ,2)
    cv2.putText(img,f'Detections/sec={times}', (0, 80), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,255),2 ,2)

# Plays sound when called 
def playsound():
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS | winsound.SND_ASYNC)


#Check if cascade_classifier file exists, else exit program
def check_cascade():
    if os.path.isfile(MODEL_PATH):
        colortext.sucsess("Cascade file found")
    else:
        colortext.danger('Cascade file not found! Shutting down...')
        exit(0)

def set_resolution(cap):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    colortext.sucsess('Resolution set')

# Main object search function
def firedetecrion():
    check_cascade()
    global FRAMERATE, SENSITIVITY
    
    fire_cascade = cv2.CascadeClassifier(MODEL_PATH)

    # TODO many devices support

    # start video capturing
    cap = cv2.VideoCapture(0)  
    colortext.sucsess('Connected to camera')

    if SETWIDTH == 1:
        set_resolution(cap)
    
    count = 0
    times_count = 0
    times_in_sec = 0
    start = time.time()
    colortext.custom('blue', '# Monitoring started #')

    # Inf loop
    while cap.isOpened():
        if time.time() - start >= 1:
            start = time.time()
            times_count = 0
            times_in_sec = 0

        ret, img = cap.read()  # capture a frame
               
        
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert image to grayscale
        fire = fire_cascade.detectMultiScale(img, 12, 5)  # test for fire detection

        display_info(img, times_in_sec)
        
        for (x, y, w, h) in fire:
            times_count+=1
            times_in_sec+=1
            # roi_gray = gray[y:y + h, x:x + w]
            # roi_color = img[y:y + h, x:x + w]
            
        
            if times_count >= SENSITIVITY * FRAMERATE * 0.01: 
                count += 1 
                colortext.warning(f'[{count}]Fire is detected ')
                cv2.putText(img,'Fire', (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,255),2 ,2)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # highlight the area of image with fire
                times_count = 0
                playsound()
                
        
        cv2.imshow('img', img)
        
        time.sleep(1/FRAMERATE)

        # If esc is pressed
        
        k = cv2.waitKey(1) & 0xff
        
        if k == 27:
            colortext.danger('# Exit button pressed #')
            break
        elif chr(k) == '[':
            if FRAMERATE > 5:
                FRAMERATE -= 5
                colortext.custom('white', f'{FRAMERATE=}')
        elif chr(k) == ']':
            if FRAMERATE < 30:
                FRAMERATE +=5
                colortext.custom('white', f'{FRAMERATE=}')
        elif chr(k) == 'k':
            if SENSITIVITY > 5:
                SENSITIVITY -= 5
        elif chr(k) == 'l':
            if SENSITIVITY < 95:
                SENSITIVITY += 5
        elif chr(k) == 's':
            cv2.imwrite(f'training/Positive-1/{uuid.uuid4()}.jpeg', img)
            colortext.sucsess('Pos saved')
        elif chr(k) == 'd':
            cv2.imwrite(f'training/Negative/{uuid.uuid4()}.jpeg', img)
            colortext.danger('Neg saved')

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    os.system('cls')
    colortext.custom('white', '# Program started #')
    # Path to your cascade_classifier
    # MODEL_PATH = 'models\cascade.xml'
    MODEL_PATH = 'cascade_out/cascade.xml'
    # Sensitivity of object search in percents
    SENSITIVITY = 1
    # Framerate for camera (check your hardware properties to set it right)
    FRAMERATE = 30
    # Size for camera (may affect searching process)
    SETWIDTH = 1
    CAMERA_WIDTH = 1280
    CAMERA_HEIGHT = 720
    # CV script that detects fire/smoke
    firedetecrion()
