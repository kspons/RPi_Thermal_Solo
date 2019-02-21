#! /usr/bin/env python2

import sys
import rospy
import cv2
import numpy as np
# from darknet_ros_msgs.msg import BoundingBoxes
from sensor_msgs.msg import Image
from std_msgs.msg import Int16MultiArray

import time

class image_segmenter:

    def __init__(self):
        # self.image_pub = rospy.Publisher("seg_img", Image)
        self.img = np.zeros((288,384), dtype=int)
        #self.th = 240
        self.image_sub = rospy.Subscriber("temperature", Int16MultiArray, callback=self.img_maker)
        
    def img_maker(self, data):
        start = time.time()
        # turn temperature data into human-viewable img
        tempData = np.reshape(data.data, (288,384))   
        temp_min = tempData.min()
        temp_max = tempData.max()
        temp_range = float(temp_max - temp_min)
        img = (tempData - temp_min) / temp_range * 255
        img = img.astype('uint8')
        # self.image = img

        # add gaus filter
        #img = cv2.GaussianBlur(img, (5,5), 0)

        # # Thresholding
        # img[tempData < -250 ] = 0

        # global 
        img[ tempData <-239 ] = 0  # pole -450

        # Jenky stuff
        img[97,282] = img[98,282]

        # save image
        # self.grey_image = img
        # img = cv2.GaussianBlur(img, (3,3), 0)
        #self.color_image = np.empty((288,384,3),dtype=np.uint8)
        #self.color_image[:,:,2] = self.color_image[:,:,1] = self.color_image[:,:,0] = img

        # self.detect_object()

        # # # Display
        # cv2.imshow('img', img)
        # waitkey = cv2.waitKey(3)

        # # # OTHER HALF BEGINS HERE (SELF.DETECT_OBJECTS())


        # find out where the sky stops in each col





        h = (img!=0).argmax(axis=0)




        # # create image of h ( where sky becomes ground at first vertical instance)
        # bw_img = np.zeros((288, 384), dtype='uint8')
        # for i in range(0, len(h)):
        #     bw_img[h[i]:, i] = 255 
        # cv2.imshow('first ground ',bw_img)
        # cv2.waitKey(3)

        # get avg of neighbor values
        omega = np.zeros(384, dtype=float)
        # ln = np.zeros(384, dtype=float)
        # rn = np.zeros(384, dtype=float)
        k = 5

        # print(stop)
        for i in range(0+k, 384-k):
            neigh = np.mean(h[i-k:i+k], dtype=float)
            omega[i] = np.abs((neigh-h[i]))/h[i]
        
        # create img of omega
        #omega_img = np.zeros((200, 384), dtype='uint8')
        #for i in range(10, 384-10):
        #    pt = 200-(omega[i]*200)
        #    if pt < 0: 
        #        pt = 0
        #    omega_img[0:int(pt), i] = 255
        
        alpha = 0.05
        #for i in range(0, 287):
        #    if omega[i] > alpha:
        #        self.color_image[1:30,i] = [250, 0, 0]                

        # cv2.imshow('no2', self.color_image)
        # cv2.waitKey(3)
        print(time.time() - start)

def main(args):
    iser = image_segmenter()
    rospy.init_node('image_segmenter', anonymous=True)
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
