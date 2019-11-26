import cv2 as cv
import time
import head as h 
# 检测人脸并绘制人脸bounding box
def getFaceBox(net, frame, conf_threshold=0.7):
    cv.waitKey(10)
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]  # 高就是矩阵有多少行
    frameWidth = frameOpencvDnn.shape[1]  # 宽就是矩阵有多少列
    blob = cv.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
    #  blobFromImage(image[, scalefactor[, size[, mean[, swap RB[, crop[, ddepth]]]]]]) -> retval  返回值   # swapRB是交换第一个和最后一个通道   返回按NCHW尺寸顺序排列的4 Mat值
    net.setInput(blob)
    detections = net.forward()  # 网络进行前向传播，检测人脸
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])  # bounding box 的坐标  
    return frameOpencvDnn, bboxes


# 网络模型  和  预训练模型/home/pi/IAD
faceProto = "/home/pi/IAD/models/opencv_face_detector.pbtxt"
faceModel = "/home/pi/IAD/models/opencv_face_detector_uint8.pb"

ageProto = "/home/pi/IAD/models/age_deploy.prototxt"
ageModel = "/home/pi/IAD/models/age_net.caffemodel"

genderProto = "/home/pi/IAD/models/gender_deploy.prototxt"
genderModel = "/home/pi/IAD/models/gender_net.caffemodel"

src = cv.imread("/home/pi/IAD/AD/SSpicture/1.jpg") #屏幕保护，即没人脸时显示
# 模型均值
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

# 加载网络
ageNet = cv.dnn.readNet(ageModel, ageProto)
genderNet = cv.dnn.readNet(genderModel, genderProto)
# 人脸检测的网络和模型
faceNet = cv.dnn.readNet(faceModel, faceProto)

# 打开一个视频文件或一张图片或一个摄像头
cap = cv.VideoCapture(0)
#cv.namedWindow("AGD",cv.WINDOW_AUTOSIZE)
padding = 20
i=0;
cv.namedWindow("advertising",cv.WINDOW_AUTOSIZE)
while cv.waitKey(1) < 0:
    # Read frame
    t = time.time()
    hasFrame, frame = cap.read()
    frame = cv.flip(frame, 1)
    if not hasFrame:
        cv.waitKey()
        break
    frameFace, bboxes = getFaceBox(faceNet, frame)
    if not bboxes:
        cv.imshow("advertising",src)
        cv.waitKey(100)
        print("No face Detected, Checking next frame")
        continue
    for bbox in bboxes:
        face = frame[max(0, bbox[1] - padding):min(bbox[3] + padding, frame.shape[0] - 1),
               max(0, bbox[0] - padding):min(bbox[2] + padding, frame.shape[1] - 1)]
        #
        blob = cv.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)   # blob输入网络进行性别的检测
        genderPreds = genderNet.forward()   # 性别检测进行前向传播
        gender = genderList[genderPreds[0].argmax()]   # 分类  返回性别类型
        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]
        if i==0:
            age_test=age
            gender_test=gender
        i=i+1;
        print(i)
        if age_test==age or gender_test==gender:
            h.advertisements(gender,age)
            print(gender,age)
        age_test=age
        gender_test=gender
        