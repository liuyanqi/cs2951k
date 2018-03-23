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
from sensor_msgs.msg import Image, PointCloud2
import sensor_msgs.point_cloud2

import cv2
from cv_bridge import CvBridge, CvBridgeError

import math

#TODO: message timestamp synchronization


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

#global variable
num_frames = 0
keep_frames = 5
pointcloud_buffer = []
# pointcloud_buffer = np.zeros((keep_frames, height, width, 3))
pointcloud_ts_buffer = []

def find_closest_timestamp(image_ts):
    global pointcloud_ts_buffer
    diff = 10000
    closest_pc = -1
    for i in range(len(pointcloud_ts_buffer)):
        if(np.abs(image_ts-pointcloud_ts_buffer[i]) < diff):
            closest_pc = i
            diff = np.abs(image_ts-pointcloud_ts_buffer[i])

    return closest_pc


def depth_to_xyz(depth_image):
    fx=367.286994337726
    fy=367.286855347968
    cx=255.165695200749
    cy=211.824600345805
    k1=0.0914203770220268
    k2=-0.269349746097515
    k3=0.0925671408453617

    pointcloud = np.zeros((height, width, 3))
    for j in range(height):
        for i in range(width):
            d = float(depth_image[j][i])/1000
            z = d
            x = (j - cx) * z /fx
            y = (i - cy) * z /fy
            pointcloud[j,i,0] = x
            pointcloud[j,i,1] = y
            pointcloud[j,i,2] = z
            # print(x,y,z)
    return pointcloud



def vis_detections(class_name, dets, thresh=0.5):
    """Draw detected bounding boxes."""
    inds = np.where(dets[:, -1] >= thresh)[0]
    if len(inds) == 0:
        return
        
    bboxes = []
    for i in inds:
        bbox = dets[i, :4]
        score = dets[i, -1]
        bboxes.append(bbox)

    return bboxes

def draw(boxes, im):
     for key, value in boxes.iteritems():
         if(value == None):
            continue
         for box in value:
             if(key == 'person'):
                cv2.rectangle(im, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
             else:
                cv2.rectangle(im, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

     cv2.imshow("Image Window", im)

def callback(data):
    time_stamp = data.header.stamp.secs
    print("get one frame: ", str(time_stamp))
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    print(cv_image.shape)
    cv2.imshow("Image Window", cv_image)
    global num_frames
    global sess
    global net
    global pointcloud_buffer
    num_frames += 1

    index = find_closest_timestamp(time_stamp)
    closest_pc = pointcloud_buffer[index]
    # if(num_frames % 5 == 0):
    scores, boxes = im_detect(sess, net, cv_image)
    CONF_THRESH = 0.8
    NMS_THRESH = 0.3
    boxes_per_class = {}
    for cls_ind, cls in enumerate(CLASSES[1:]):
        cls_ind += 1 # because we skipped background
        if(cls == 'chair' or cls == 'person'):
            cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)]
            cls_scores = scores[:, cls_ind]
            dets = np.hstack((cls_boxes, cls_scores[:, np.newaxis])).astype(np.float32)
            keep = nms(dets, NMS_THRESH)
            dets = dets[keep, :]
            boxes_per_class[cls] = vis_detections(cls, dets, thresh=CONF_THRESH)
            for box in boxes_per_class[cls]:
                centroid_x = int(float(box[0]+box[2])/2)
                centroid_y = int(float(box[1]+box[3])/2)
                print(cls)
                print(closest_pc[centroid_x, centroid_y])
        
        # print(boxes_per_class)
        draw(boxes_per_class, cv_image)


    cv2.waitKey(3)

def callback_pc(data):
    print("get depth image: ", str(data.header.stamp.secs))
    cv_depth = bridge.imgmsg_to_cv2(data, desired_encoding="16UC1")
    pt = depth_to_xyz(cv_depth)
    global pointcloud_buffer
    global pointcloud_ts_buffer
    if len(pointcloud_buffer) == 5:
        pointcloud_buffer.pop()
        pointcloud_ts_buffer.pop()
    pointcloud_buffer.append(pt)
    pointcloud_ts_buffer.append(data.header.stamp.secs)
    # for y in range(480):
    #     for x in range(640):
    #         print(cv_depth[y * 640 + x])
    # print(data.header.stamp.secs)
    #for point in sensor_msgs.point_cloud2.read_points(data, skip_nans=True):
    #    print(point[0], point[1], point[2])

def listener():
    print("listening")
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("/kinect2/qhd/image_color_rect", Image, callback)
    rospy.Subscriber("/kinect2/qhd/image_depth_rect", Image, callback_pc)
    rospy.spin()

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--net', dest='demo_net', help='Network to use [vgg16 res101]',
                        choices=NETS.keys(), default='res101')
    parser.add_argument('--dataset', dest='dataset', help='Trained dataset [pascal_voc pascal_voc_0712]',
                        choices=DATASETS.keys(), default='pascal_voc_0712')
    args = parser.parse_args()

    return args
if __name__ == '__main__':
    cfg.TEST.HAS_RPN = True  # Use RPN for proposals
    args = parse_args()

    # model path
    demonet = args.demo_net
    dataset = args.dataset
    tfmodel = os.path.join('output', demonet, DATASETS[dataset][0], 'default',
                              NETS[demonet][0])


    if not os.path.isfile(tfmodel + '.meta'):
        raise IOError(('{:s} not found.\nDid you download the proper networks from '
                       'our server and place them properly?').format(tfmodel + '.meta'))



    # init session
    #sess = tf.Session(config=tfconfig)
    # load network
    '''if demonet == 'vgg16':
        net = vgg16()
    elif demonet == 'res101':
        net = resnetv1(num_layers=101)
    else:
        raise NotImplementedError
    net.create_architecture("TEST", 21,
                          tag='default', anchor_scales=[8, 16, 32])'''
    saver = tf.train.Saver()
    saver.restore(sess, tfmodel)
    print("model loaded")
    listener()
