import rospy
from visualization_msgs.msg import Marker

def add_point(frame_id='map', id_=0, x=0, y=0, r=0,g=0,b=0, scale=0.1):
    marker = Marker()
    marker.header.frame_id = frame_id
    marker.header.stamp = rospy.get_rostime()
    marker.ns = "my_namespace"
    marker.id = id_
    marker.type = marker.SPHERE
    marker.action = marker.ADD
    marker.pose.position.x = x
    marker.pose.position.y = y
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = scale
    marker.scale.y = scale
    marker.scale.z = scale
    marker.color.a = 1.0 
    marker.color.r = r
    marker.color.g = g
    marker.color.b = b
    marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae"
    return marker

def add_text(frame_id='map', id_=0, x=0, y=0, r=0,g=0,b=0, scale=0.1):
    marker = Marker()
    marker.header.frame_id = frame_id
    marker.header.stamp = rospy.get_rostime()
    marker.ns = "my_namespace"
    marker.id = id_
    marker.type = marker.TEXT_VIEW_FACING
    marker.action = marker.ADD
    marker.pose.position.x = x+0.1
    marker.pose.position.y = y+0.1
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.text = "chair" + str(int(id_/2))
    marker.scale.x = scale
    marker.scale.y = scale
    marker.scale.z = scale
    marker.color.a = 1.0 
    marker.color.r = r
    marker.color.g = g
    marker.color.b = b
    marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae"
    return marker

