#!/usr/bin/env python     #在文件头部 ( 第一行 ) 加上   设置 Python 解释器  

# -*- coding: utf-8 -*-  #在文件头部 ( 第二行 ) 加上   在编辑器中设置以 UTF-8 默认编码保存文件  
 

import cv2 as cv
import numpy as np
import glob
import random

##############################展示广告图片#########################################
#cv.namedWindow("advertising",cv.WINDOW_AUTOSIZE)  #定义窗口 /以一个参数是窗口名称 //第二个参数是窗口形式
#cv.resizeWindow("advertising",1000,1500)
def read_file(path_file_number):
    if path_file_number == []:
      print("未找到广告文件")
    else:
        num =random.randint(0,len(path_file_number))
        src = cv.imread(path_file_number[num])
        cv.imshow("advertising",src)
        cv.waitKey(50)
###################################################################################
def video_input(path_file_video_number):  #定义视频函数
    if path_file_video_number == []:
      print("未找到广告文件")
    else:
        num =random.randint(0,len(path_file_video_number)-1)
        capture = cv.VideoCapture(path_file_video_number[num]) #打开摄像头 /参数是数字表示摄像头 也可以是视频路径
        while(True):  #循环 /无限循环
            ret , frame = capture.read()  #获取视频信息 \第一个返回值表示视频状态 \第二个返回值表示每一帧画面
            if ret == False:
                break
#             frame = np.flip(frame,1)  #对画面进行颠倒 /画面信息 //1：左右，-1上下
            cv.imshow("advertising",frame)  #展示图片信息
            cv.waitKey(10)
##################################对应女性的广告投放################################
def Male_0_2():
    path_file_number=glob.glob("/home/pi/IAD/AD/Male/0_2/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Male/0_2/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Male_4_6():
    path_file_number=glob.glob("/home/pi/IAD/AD/Male/4_6/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Male/4_6/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Male_8_12():
    path_file_number=glob.glob("/home/pi/IAD/AD/Male/8_12/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Male/8_12/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Male_15_20():
    path_file_number=glob.glob("/home/pi/IAD/AD/Male/15_20/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Male/15_20/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Male_25_32():
    path_file_number=glob.glob("/home/pi/IAD/AD/Male/25_32/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Male/25_32/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Male_38_43():
    path_file_number=glob.glob("/home/pi/IAD/AD/Female/38_43/*.jpg") #获取当前文件夹下文
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Female/38_43/*.mp4") #获取当前文件夹下文
    video_input(path_file_video_number)
    read_file(path_file_number)

def Male_48_53():
    path_file_number=glob.glob("/home/pi/IAD/AD/Male/48_53/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Male/48_53/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Male_60_100():
    path_file_number=glob.glob("/home/pi/IAD/AD/Male/60_100/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Male/60_100/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

###################################################################################

##################################对应男性的广告投放################################
def Female_0_2():
    path_file_number=glob.glob("/home/pi/IAD/AD/Female/0_2/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Female/0_2/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Female_4_6():
    path_file_number=glob.glob("/home/pi/IAD/AD/Female/4_6/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Female/4_6/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Female_8_12():
    path_file_number=glob.glob("/home/pi/IAD/AD/Female/8_12/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Female/8_12/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Female_15_20():
    path_file_number=glob.glob("/home/pi/IAD/AD/Female/15_20/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Female/15_20/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Female_25_32():
    path_file_number=glob.glob("/home/pi/IAD/AD/Female/25_32/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Female/25_32/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Female_38_43():
    path_file_number=glob.glob("/home/pi/IAD/AD/Female/38_43/*.jpg") #获取当前文件夹下文
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Female/38_43/*.mp4") #获取当前文件夹下文
    video_input(path_file_video_number)
    read_file(path_file_number)

def Female_48_53():
    path_file_number=glob.glob("/home/pi/IAD/AD/Female/48_53/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Female/48_53/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

def Female_60_100():
    path_file_number=glob.glob("/home/pi/IAD/AD/Female/60_100/*.jpg") #获取当前文件夹下文件
    path_file_video_number=glob.glob("/home/pi/IAD/AD/Female/60_100/*.mp4") #获取当前文件夹下文件
    video_input(path_file_video_number)
    read_file(path_file_number)

#######################################################################################


###################################根据性别和年龄播放相应广告###########################
def advertisements(Gender,Age):
####################################男性###############################################
    if Gender == "Male":
        if Age =="(0-2)":
            Male_0_2()

        if Age =="(4-6)":
            Male_4_6()

        if Age =="(8-12)":
            Male_8_12()

        if Age =="(15-20)":
            Male_15_20()

        if Age =="(25-32)":
            Male_25_32()

        if Age =="(38-43)":
            Male_38_43()

        if Age =="(48-53)":
            Male_48_53()

        if Age =="(60-100)":
            Male_60_100()
        
#####################################女性################################################
    elif Gender == "Female":
        if Age =="(0-2)":
            Female_0_2()

        if Age =="(4-6)":
            Female_4_6()

        if Age =="(8-12)":
            Female_8_12()

        if Age =="(15-20)":
            Female_15_20()

        if Age =="(25-32)":
            Female_25_32()

        if Age =="(38-43)":
            Female_38_43()

        if Age =="(48-53)":
            Female_48_53()

        if Age =="(60-100)":
            Female_60_100()
#######################################################################################


# import sys   

# reload(sys)   

# sys.setdefaultencoding('utf-8')