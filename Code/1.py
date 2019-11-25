import cv2 as cv #导入opencv———cv2 库命名为cv
import numpy as np  #导入numpy库，命名为np

#图片展示和调用摄像头#

def video_input():  #定义视频函数
    capture = cv.VideoCapture(0) #打开摄像头 /参数是数字表示摄像头 也可以是视频路径
    cv.namedWindow("video show",cv.WINDOW_AUTOSIZE)  #定义窗口 /以一个参数是窗口名称 //第二个参数是窗口形式
    while(True):  #循环 /无限循环
         ret , frame = capture.read()  #获取视频信息 \第一个返回值表示视频状态 \第二个返回值表示每一帧画面
         if ret == False:
            break
         frame = np.flip(frame,1)  #对画面进行颠倒 /画面信息 //1：左右，-1上下
         cv.imshow("video show",frame)  #展示图片信息
         c = cv.waitKey(50)
         if c == 27:
             break
   

print("*************hello python**************")
src = cv.imread("/home/pi/IAD/AD/SSpicture/1.jpg") #获取图片 /参数图片路径
cv.namedWindow("image show",cv.WINDOW_AUTOSIZE)  #定义窗口 /以一个参数是窗口名称 //第二个参数是窗口形式
cv.imshow("image show",src)
#video_input()

cv.waitKey(0)  #等待 /参数表示时间 0表示一直等待
cv.destroyAllWindows() #销毁所有窗口
