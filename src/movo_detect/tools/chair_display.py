
import rospy
import actionlib
import math
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import pickle
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from tf import TransformListener 
from thread import start_new_thread


def talker():

    rospy.init_node("talker", anonymous=True)
    global pub
    global markerArray
    pub = rospy.Publisher('chair', MarkerArray, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(markerArray)
        rate.sleep()




def listener():
    print("listening")
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("/kinect2/qhd/image_color_rect", Image, callback, queue_size=3)
    rospy.spin()



if __name__ == '__main__':

    global chair_info
    global markerArray
    markerArray = MarkerArray()
    with open('chair_info.pkl', 'rb') as f:
        chair_info = pickle.load(f)
    print(len(chair_info))
    for chair in chair_info:
        marker = Marker()
        marker.header.frame_id = chair['header_frame_id']
        marker.header.stamp = chair['header_header_stamp']
        marker.id = chair['id']
        marker.ns = chair['namespace']
        marker.type = chair['type']
        marker.action  = chair['action']
        marker.pose.position.x = chair['pose_position_x']
        marker.pose.position.y = chair['pose_position_y']
        marker.pose.position.z = chair['pose_position_z']
        marker.pose.orientation.x = chair['pose_orientation_x']
        marker.pose.orientation.y = chair['pose_orientation_y']
        marker.pose.orientation.z = chair['pose_orientation_z']
        marker.pose.orientation.w = chair['pose_orientation_w']
        marker.scale.x = 0.1
        marker.scale.y = 0.1
        marker.scale.z = 0.1
        marker.color.a = 1.0 
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0

        marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae"

        markerArray.markers.append(marker)

    talker()