# -*- coding: utf-8 -*-

# @author leone
# @desc 使用 python 的 openCV 获取网络摄像头的数据
# @version 2018-12-23

import cv2
import sys

# 根据摄像头设置IP及rtsp端口
url = 'rtsp://admin:admin@192.168.0.25:554/11'

# 读取视频流
cap = cv2.VideoCapture(url)
# 设置视频参数
cap.set(3, 480)

# 设置摄像头的帧大小
cap.set(cv2.CAP_PROP_FPS, 90)

print(cap.isOpened())

print(sys.version)

print(cv2.__version__)

while cap.isOpened():
    ret_flag, img_camera = cap.read()
    cv2.imshow("camera", img_camera)

    # 每帧数据延时 1ms, 延时为0, 读取的是静态帧
    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite("test.jpg", img_camera)
    if k == ord('q'):
        break

# 释放所有摄像头
cap.release()

# 删除窗口
cv2.destroyAllWindows()
