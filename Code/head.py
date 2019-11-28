#!/usr/bin/env python     #在文件头部 ( 第一行 ) 加上   设置 Python 解释器  

# -*- coding: utf-8 -*-  #在文件头部 ( 第二行 ) 加上   在编辑器中设置以 UTF-8 默认编码保存文件  

##############################展示广告图片#########################################

import cv2 as cv
import numpy as np
import glob
import random

##############################展示广告图片#########################################
cv.namedWindow("advertising",cv.WINDOW_AUTOSIZE)  #定义窗口 /以一个参数是窗口名称 //第二个参数是窗口形式
cv.resizeWindow("advertising",1000,1500)
def read_file(path_file_number):
    if path_file_number == []:
      print("未找到图片文件")
    else:
        num =random.randint(0,len(path_file_number)-1)
        src = cv.imread(path_file_number[num])
        cv.imshow("advertising",src)
        cv.waitKey(3000)
###################################################################################
def video_input(path_file_video_number):  #定义视频函数
    if path_file_video_number == []:
      print("未找到视频文件")
    else:
        num =random.randint(0,len(path_file_video_number)-1)
        capture = cv.VideoCapture(path_file_video_number[num]) #打开摄像头 /参数是数字表示摄像头 也可以是视频路径
        while(True):  #循环 /无限循环
            ret , frame = capture.read()  #获取视频信息 \第一个返回值表示视频状态 \第二个返回值表示每一帧画面
            if ret == False:
                break
            cv.imshow("advertising",frame)  #展示图片信息
            cv.waitKey(50)
##################################对应女性的广告投放################################
def aaa(path_file_video_number,path_file_number,a):
    if a%10:
        video_input(path_file_video_number)
    if a//10:
        read_file(path_file_number)
        

def advertisements(Gender,Age,aa):
####################################男性###############################################
    if Gender == "Male":
        if Age =="(0-2)":
            number=glob.glob("/home/pi/IAD/AD/Male/0_2/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Male/0_2/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(4-6)":
            number=glob.glob("/home/pi/IAD/AD/Male/4_6/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Male/4_6/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(8-12)":
            number=glob.glob("/home/pi/IAD/AD/Male/8_12/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Male/8_12/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(15-20)":
            number=glob.glob("/home/pi/IAD/AD/Male/15_20/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Male/15_20/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(25-32)":
            number=glob.glob("/home/pi/IAD/AD/Male/25_32/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Male/25_32/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(38-43)":
            number=glob.glob("/home/pi/IAD/AD/Male/38_43/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Male/38_43/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(48-53)":
            number=glob.glob("/home/pi/IAD/AD/Male/48_53/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Male/48_53/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(60-100)":
            number=glob.glob("/home/pi/IAD/AD/Male/60_100/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Male/60_100/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)
        
#####################################女性################################################
    elif Gender == "Female":
        if Age =="(0-2)":
            number=glob.glob("/home/pi/IAD/AD/Female/0_2/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Female/0_2/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(4-6)":
            number=glob.glob("/home/pi/IAD/AD/Female/4_6/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Female/4_6/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(8-12)":
            number=glob.glob("/home/pi/IAD/AD/Female/8_12/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Female/8_12/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(15-20)":
            number=glob.glob("/home/pi/IAD/AD/Female/15_20/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Female/15_20/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(25-32)":
            number=glob.glob("/home/pi/IAD/AD/Female/25_32/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Female/25_32/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(38-43)":
            number=glob.glob("/home/pi/IAD/AD/Female/38_43/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Female/38_43/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(48-53)":
            number=glob.glob("/home/pi/IAD/AD/Female/48_53/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Female/48_53/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)

        if Age =="(60-100)":
            number=glob.glob("/home/pi/IAD/AD/Female/60_100/*.jpg") #获取当前文件夹下文件
            video=glob.glob("/home/pi/IAD/AD/Female/60_100/*.mp4") #获取当前文件夹下文件
            aaa(video,number,aa)
#######################################################################################
#advertisements("Female","(48-53)",10)
#######################################################################################

# import sys   

# reload(sys)   

# sys.setdefaultencoding('utf-8')

