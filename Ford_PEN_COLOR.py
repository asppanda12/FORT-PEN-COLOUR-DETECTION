import cv2
import numpy as np
cap1=cv2.VideoCapture(0)
while True:
     sucess,cap=cap1.read()
     img_hsv=cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)
     
  
    
     l_g_mask=cv2.inRange(img_hsv,(36,161,134),(80,255,255))
     l_g_mask=cv2.GaussianBlur(l_g_mask,(5,5),0)
   
     pi_mask=cv2.inRange(img_hsv,(101,0,130),(179,255,226))
   
     g_mask=cv2.inRange(img_hsv,(102,0,102),(119,175,230))
     g_mask=cv2.GaussianBlur(g_mask,(5,5),0)
   

     pu_mask=cv2.inRange(img_hsv,(120,51,0),(148,255,111))
     pu_mask=cv2.GaussianBlur(pu_mask,(5,5),0)
   

     d_g_mask=cv2.inRange(img_hsv,(69,0,0),(110,255,243))
     d_g_mask=cv2.GaussianBlur(d_g_mask,(5,5),0)
    
     
     ing=cv2.imshow("outp",pi_mask)

     imgd=cv2.imshow("output",pi_mask)
     contours, hierarchy = cv2.findContours(pi_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
     for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 5000 and area <10000):
            
            
            x, y, w, h = cv2.boundingRect(contour)
            cap = cv2.rectangle(cap, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(cap, "Pink Colour FORT PEN", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255)) 
     contours1, hierarchy = cv2.findContours(l_g_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE) 
     
     for pic, contour in enumerate(contours1):
        area = cv2.contourArea(contour)
        if(area > 1000 and area <10000):      
            x, y, w, h = cv2.boundingRect(contour)
            cap = cv2.rectangle(cap, (x, y), 
                                       (x + w, y + h), 
                                       (0, 255,0), 2)
              
            cv2.putText(cap, "LIGHT GREEN FORT PEN", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 255, 0)) 

     contours2, hierarchy = cv2.findContours(g_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE) 
     
     for pic, contour in enumerate(contours2):
        area = cv2.contourArea(contour)
        if(area > 3000 and area <10000):      
            x, y, w, h = cv2.boundingRect(contour)
            cap = cv2.rectangle(cap, (x, y), 
                                       (x + w, y + h), 
                                       (128,128,128), 2)
              
            cv2.putText(cap, "GREY COLOR FORT PEN", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (128,128,128)) 
     contours3, hierarchy = cv2.findContours(pu_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE) 
     
     for pic, contour in enumerate(contours3):
        area = cv2.contourArea(contour)
        if(area > 5000 and area <10000):      
            x, y, w, h = cv2.boundingRect(contour)
            cap = cv2.rectangle(cap, (x, y), 
                                       (x + w, y + h), 
                                       (149,53,83), 2)
              
            cv2.putText(cap, "PURPLE COLOR FORT PEN", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (143,53,83)) 
    

     contours4, hierarchy = cv2.findContours(d_g_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE) 
     
     



     imgo=cv2.imshow("output11",cap)
     p=cv2.waitKey(1)
     if(p==27):
         break