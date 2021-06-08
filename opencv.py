import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np
import sqlite3
import webbrowser
conn=sqlite3.connect('database.sqlite')
cur=conn.cursor()

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
abc=1
while abc>0:
    sucess,img=cap.read()
    for barcode in pyzbar.decode(img):
        mydata=barcode.data.decode()
        cur.execute('''Select * from PRODUCT where Code=?''',(mydata,) )
        n=cur.fetchone()
        if n==None:
            print("not Found")
        else:
            for element in n:
                print(element)
        abc=abc-1

    cv2.imshow("Result:",img)
    cv2.waitKey(1)
