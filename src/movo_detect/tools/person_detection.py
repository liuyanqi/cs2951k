#!/usr/bin/python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import _init_paths
from model.config import cfg
from model.test import im_detect
from model.nms_wrapper import nms

from utils.timer import Timer
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os, cv2
import argparse

from nets.vgg16 import vgg16
from nets.resnet_v1 import resnetv1

import rospy
from sensor_msgs.msg import Image, PointCloud2, CameraInfo
import sensor_msgs.point_cloud2
from geometry_msgs.msg import PointStamped

import cv2
from cv_bridge import CvBridge, CvBridgeError

import math
from std_msgs.msg import Int32

from tf import TransformListener 


bridge = CvBridge()

CLASSES = ('__background__',
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor')

NETS = {'vgg16': ('vgg16_faster_rcnn_iter_70000.ckpt',),'res101': ('res101_faster_rcnn_iter_110000.ckpt',)}
DATASETS= {'pascal_voc': ('voc_2007_trainval',),'pascal_voc_0712': ('voc_2007_trainval+voc_2012_trainval',)}


#image
height = 540
width = 960

# set config
tfconfig = tf.ConfigProto(allow_soft_placement=True)
tfconfig.gpu_options.allow_growth=True
sess = tf.Session(config=tfconfig)
net = resnetv1(num_layers=101)
net.create_architecture("TEST", 21, tag='default', anchor_scales=[8, 16, 32])
people_counter = 0

def vis_detections(class_name, dets, thresh=0.5):
    inds = np.where(dets[:, -1] >= thresh)[0]
    if len(inds) == 0:
        return
        
    bboxes = []
    for i in inds:
        bbox = dets[i, :4]
        score = dets[i, -1]
        bboxes.append(bbox)

    return bboxes
def callback(data):
    #process RGB image
    time_stamp = data.header.stamp.secs
    print("get one frame: ", str(time_stamp))
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    print(cv_image.shape)
    cv2.imshow("Image Window", cv_image)
    global sess
    global net
    global people_counter

    scores, boxes = im_detect(sess, net, cv_image)
    CONF_THRESH = 0.8
    NMS_THRESH = 0.3
    boxes_per_class = {}
    for cls_ind, cls in enumerate(CLASSES[1:]):
        cls_ind += 1 # because we skipped background
        if(cls == 'person'):
            cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)]
            cls_scores = scores[:, cls_ind]
            dets = np.hstack((cls_boxes, cls_scores[:, np.newaxis])).astype(np.float32)
            keep = nms(dets, NMS_THRESH)
            dets = dets[keep, :]
            boxes_per_class[cls] = vis_detections(cls, dets, thresh=CONF_THRESH)
            if boxes_per_class[cls] == None:
                continue
            for box in boxes_per_class[cls]:
                #look at the 5X5 point around centroid, find out one has non zero depth and less than 4m far away
                centroid_x = int(float(box[0]+box[2])/2)
                centroid_y = int(float(box[1]+box[3])/2)
                if centroid_y > width/2 - 40 and centroid_y < width/2 + 40:
                	people_counter += 1

    print(people_counter)
    global pub
    pub.publish(people_counter)

    cv2.waitKey(3)

def listener():
    print("listening")
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("/kinect2/qhd/image_color_rect", Image, callback, queue_size=3)
    global pub 
    pub = rospy.Publisher('person', Int32, queue_size=10)
    rospy.spin()



if __name__ == '__main__':
    cfg.TEST.HAS_RPN = True  # Use RPN for proposals

    # model path
    demonet = 'res101'
    dataset = 'pascal_voc_0712'
    tfmodel = os.path.join('output', demonet, DATASETS[dataset][0], 'default',
                              NETS[demonet][0])

    if not os.path.isfile(tfmodel + '.meta'):
        raise IOError(('{:s} not found.\nDid you download the proper networks from '
                       'our server and place them properly?').format(tfmodel + '.meta'))

    saver = tf.train.Saver()
    saver.restore(sess, tfmodel)
    print("model loaded")
    listener()
