# coding:utf8

# @author leone
# @desc OpenCV 调用摄像头,默认调用笔记本摄像头
# @version 2018-12-13

from datetime import datetime
import cv2

# 通过rtsp协议打开网络摄像头
cap = cv2.VideoCapture('rtsp://admin:admin@192.168.0.25:554/25')

# 打开本机摄像头
# cap = cv2.VideoCapture(0)

# 设置视频参数: propId: 设置的视频参数, value: 设置的参数值
cap.set(3, 480)

# cap.isOpened() 返回 true/false, 检查摄像头初始化是否成功
while cap.isOpened():
    ret_flag, img_camera = cap.read()
    cv2.imshow("camera", img_camera)

    # 每帧数据延时 1ms, 延时为0, 读取的是静态帧
    k = cv2.waitKey(1)

    # 按下 's' 保存截图
    if k == ord('s'):
        filename = 'screenshot/{0}.jpg'.format(datetime.now().strftime('%y%m%d%H%m%S'))
        print(filename)
        cv2.imwrite(filename, img_camera)

    # 按下 'q' 退出
    if k == ord('q'):
        break

# 释放所有摄像头
cap.release()

# 删除建立的所有窗口
cv2.destroyAllWindows()
