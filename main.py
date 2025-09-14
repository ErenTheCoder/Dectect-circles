import cv2
import numpy as np



def dectect_circles_hough(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.medianBlur(gray, 5)


    cirlces = cv2.HoughCircles(gray_blurred,
                               cv2.HOUGH_GRADIENT,
                               dp=1,
                               minDist=20,
                               param1=50,
                               param2=30,
                               minRadius=10,
                               maxRadius=80)
    
    count = 0
    if circles is not None:
        circles = np.uint16(np.around(circles))
        count = len(circles[0, :])
        for (x,y,r) in circles[0, :]:
            cv2.circle(img, (x,y), r,(0,255,0), 2)
            cv2.circle(img, (x,y), 2, (0,0,255), 3)

    print(f"[HoughCircles] Number Of Circles Detected: {count}")
    cv2.imshow("HoughCircles Results", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return count





    




    

