# -*- coding:utf-8 -*-
# @Time    :2022/8/11 9:21
# @Author  :紫菜蛋花汤
# @File    :Map.py
# @Software:PyCharm

import cv2
import numpy as np
class MapCreat():
    def StratAndEnd(self, img):
        #取决于原先的图像是否为灰度图像
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.medianBlur(gray_img,3)
        circles = cv2.HoughCircles(gray_img, method=cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                                   param1=100, param2=20, minRadius=10, maxRadius=200)
        #画圆的时候要注意对于参数的调整
        #由于是对于最终的图像进行调整，可以人为的加一些约束
        circles = np.uint16(np.around(circles))#提取为二维因为对于图像的像素点没有小数
        # for i in circles[0, :]:
        #     cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)  # 画圆
        #     cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 10)  # 画圆心
        if circles[0, 0, 0] < circles[0, 1, 0]:
            start = circles[0, 0, :]
            end = circles[0, 1, :]
        else:
            start = circles[0, 1, :]
            end = circles[0, 0, :]
        return [start,end]
    def obstacle(self, img):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)
        map = thresh / 255
        return map
# if __name__ == '__main__':
#     globalmap = Map()
#     img = cv2.imread('3.jpg')
#     start = globalmap.StratAndEnd(img)[0]
#     end = globalmap.StratAndEnd(img)[1]
#     imgout = globalmap.obstacle(img)
#     cv2.circle(imgout, (start[0], start[1]), 10, (255, 255, 0), 2)
#     cv2.circle(imgout, (end[0], end[1]), 10, (255, 255, 0), 2)
#     cv2.imshow('1', imgout)
#     cv2.waitKey()

