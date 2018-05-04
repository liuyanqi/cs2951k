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
from visualization_msgs.msg import MarkerArray
from marker import add_point
from marker import add_text


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

#global variable
num_frames = 0
keep_frames = 5
#NOTE: pointcloud_buffer is acutally depth image
pointcloud_buffer = []
# pointcloud_buffer = np.zeros((keep_frames, height, width, 3))
pointcloud_ts_buffer = []
pointcloud = np.zeros((height, width, 3))
markerArray = MarkerArray()


def find_closest_timestamp(image_ts):
    global pointcloud_ts_buffer
    diff = 10000
    closest_pc = -1
    for i in range(len(pointcloud_ts_buffer)):
        if(np.abs(image_ts-pointcloud_ts_buffer[i]) < diff):
            closest_pc = i
            diff = np.abs(image_ts-pointcloud_ts_buffer[i])

    print(pointcloud_ts_buffer[closest_pc])
    print(diff)
    return closest_pc

def depth_to_xyz(depth, j, i):
    fx=540.68603515625
    fy=540.68603515625
    cx=479.75
    cy=269.75

    d = float(depth)/1000
    z = d
    x = (j - cx) * z /fx
    y = -(i - cy) * z /fy
    return(x,y,z)


# def depth_to_xyz(depth_image):
#     fx=540.68603515625
#     fy=540.68603515625
#     cx=479.75
#     cy=269.75

#     global pointcloud
#     #pointcloud = np.zeros((height, width, 3))
#     for j in range(height):
#         for i in range(width):
#             d = float(depth_image[j][i])/1000
#          
#   z = d
#             x = (j - cx) * z /fx
#             y = (i - cy) * z /fy
#             pointcloud[j,i,0] = x
#             pointcloud[j,i,1] = y
#             pointcloud[j,i,2] = z
#             # print(x,y,z)
#     return pointcloud



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

def draw(boxes, valid_chair_boxes, im):
     for key, value in boxes.iteritems():
         if(value == None):
            continue
         for box in value:
             if(key == 'person'):
                cv2.rectangle(im, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
             else:
                cv2.rectangle(im, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                center_x = (box[0] + box[2])/2
                center_y = (box[1] + box[3])/2

                cv2.circle(im, (int(center_x), int(center_y)), 1, (0,255,0))

     for idx, chair in enumerate(valid_chair_boxes):
        cv2.putText(im, 'Chair'+str(idx), (chair[0],chair[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 2)

     cv2.imshow("Image Window", im)

def add_markerArray(marker, marker_text):
    global markerArray
    find_similar = False
    for m in markerArray.markers:
        distance = (m.pose.position.x - marker.pose.position.x)**2 + (m.pose.position.y - marker.pose.position.y)**2
        distance = math.sqrt(distance)
        if distance < 1:
            find_similar = True
            break
    if not find_similar:
        markerArray.markers.append(marker)
        markerArray.markers.append(marker_text)



def callback(data):
    #process RGB image
    time_stamp = data.header.stamp.secs
    print("get one frame: ", str(time_stamp))
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    print(cv_image.shape)
    global num_frames
    global sess
    global net
    global pointcloud_buffer
    global markerArray
    num_frames += 1
    chair_counter = 0


    #find ros transform
    tflistener.waitForTransform("/base_link", "/map", rospy.Time(0), rospy.Duration(4.0))
    # t = tflistener.getLatestCommonTime("/base_link", "/map")
    # position, quaternion = tflistener.lookupTransform("/base_link", "/map", t)
    # print(position, quaternion)

    index = find_closest_timestamp(time_stamp)
    closest_pc = pointcloud_buffer[index]
    scores, boxes = im_detect(sess, net, cv_image)
    CONF_THRESH = 0.8
    NMS_THRESH = 0.3
    boxes_per_class = {}
    valid_chair_box = []
    for cls_ind, cls in enumerate(CLASSES[1:]):
        cls_ind += 1 # because we skipped background
        if(cls == 'chair' or cls == 'person'):
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
                breakout = 0
                for i in range(max(centroid_x-5, 0), min(centroid_x+5, width)):
                    if(breakout):
                        breakout = 0
                        break
                    for j in range(max(centroid_y-5,0), min(centroid_y+5, height)):
                        x, y,z = depth_to_xyz(closest_pc[centroid_y, centroid_x], centroid_y, centroid_x)
                        if z !=0 and z < 4:
                            if cls == 'chair':
                                print(cls)
                                print(x,y,z)
                                valid_chair_box.append(box)
                                chair_point = PointStamped()
                                chair_point.header.frame_id = "kinect2_link"
                                chair_point.point.x = z
                                chair_point.point.y = y
                                chair_point.point.z = x
                                # transform the chair location to map frame
                                p = tflistener.transformPoint("map", chair_point)

                                #create marker for the chair and check if we need to add it to global marker array
                                marker = add_point(frame_id="map", id_=len(markerArray.markers), x=p.point.x, y=p.point.y, scale=0.1, b=1)
                                marker_text = add_text(frame_id="map", id_=len(markerArray.markers)+1, x=p.point.x, y=p.point.y, scale=0.2, b=1)
                                add_markerArray(marker, marker_text)
                                chair_counter+=1
                            breakout=1
                            break


        #bbox visualization
        draw(boxes_per_class, valid_chair_box, cv_image)
        #publish marker array
        global pub
        print("MarkerArray size: ", len(markerArray.markers)/2)
        pub.publish(markerArray)


    cv2.waitKey(3)

def callback_pc(data):
    #save depth image into buffer for future use
    print("get depth image: ", str(data.header.stamp.secs))
    cv_depth = bridge.imgmsg_to_cv2(data, desired_encoding="16UC1")
    global pointcloud_buffer
    global pointcloud_ts_buffer
    if len(pointcloud_buffer) == 5:
        pointcloud_buffer.pop()
        pointcloud_ts_buffer.pop()
    pointcloud_buffer.append(cv_depth)
    pointcloud_ts_buffer.append(data.header.stamp.secs)


def listener():
    print("listening")
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("/kinect2/qhd/image_color_rect", Image, callback, queue_size=3)
    rospy.Subscriber("/kinect2/qhd/image_depth_rect", Image, callback_pc, queue_size=3)
    global pub 
    pub = rospy.Publisher('chair', MarkerArray, queue_size=10)
    global tflistener
    tflistener = TransformListener()
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
