import cv2 
import numpy as np 
  
img = cv2.imread('motor.jpg', cv2.IMREAD_COLOR) 
cv2.imshow('Original', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gris', gray) 
cv2.waitKey(0)

gray_blurred = cv2.blur(gray, (9, 9)) 
cv2.imshow('Borrosa', gray_blurred )
cv2.waitKey(0)

detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 2, maxRadius =30) 
  
if detected_circles is not None: 
  
    
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
        
        print("Centro ({:}, {:}), radio = {:}".format(a, b, r))
  
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
		
        cv2.imshow("Detección de circunferencias", img) 
        cv2.waitKey(0) 
        
cv2.destroyAllWindows()