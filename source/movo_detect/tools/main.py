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

bridge = CvBridge()

CLASSES = ('__background__',
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor')

NETS = {'vgg16': ('vgg16_faster_rcnn_iter_70000.ckpt',),'res101': ('res101_faster_rcnn_iter_110000.ckpt',)}
DATASETS= {'pascal_voc': ('voc_2007_trainval',),'pascal_voc_0712': ('voc_2007_trainval+voc_2012_trainval',)}

# set config
tfconfig = tf.ConfigProto(allow_soft_placement=True)
tfconfig.gpu_options.allow_growth=True
sess = tf.Session(config=tfconfig)
net = resnetv1(num_layers=101)

net.create_architecture("TEST", 21, tag='default', anchor_scales=[8, 16, 32])
num_frames = 0

def vis_detections(im, class_name, dets, thresh=0.5):
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
         for box in value:
             cv2.rectangle(im, (box[0], box[1]), (box[3], box[4]), (255, 0, 0), 2)

     cv2.imshow("Image Window", im)

def callback(data):
    print("get one frame")
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    # cv2.imshow("Image Window", cv_image)
    num_frames += 1
    if(num_frames % 5 == 0):
        scores, boxes = im_detect(sess, net, cv_image)
        CONF_THRESH = 0.8
        NMS_THRESH = 0.3
        boxes_per_class = {}
        for cls_ind, cls in enumerate(CLASSES[1:]):
            cls_ind += 1 # because we skipped background
            cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)]
            cls_scores = scores[:, cls_ind]
            dets = np.hstack((cls_boxes,
                          cls_scores[:, np.newaxis])).astype(np.float32)
            keep = nms(dets, NMS_THRESH)
            dets = dets[keep, :]
            boxes_per_class[cls] = vis_detections(im, cls, dets, thresh=CONF_THRESH)

        draw(boxes_per_class, cv_image)


    cv2.waitKey(3)

def callback_pc(data):
    print("get point cloud")
    for point in sensor_msgs.point_cloud2.read_points(data, skip_nans=True):
        print(point[0], point[1], point[2])

def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("/kinect2/qhd/image_color_rect", Image, callback)
    # rospy.Subscriber("/kinect2/qhd/points", PointCloud2, callback_pc)
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

    listener()