import rospy
from sensor_msgs.msg import Image, PointCloud2, CameraInfo
import sensor_msgs.point_cloud2
from geometry_msgs.msg import PointStamped
import pickle
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker

def callback(data):
	markerarray_info =[]
	print("here")
	output = open('chair_info.pkl', 'wb')
	for m in data.markers:
		marker_info = {}
		marker_info['header_frame_id'] = m.header.frame_id
		marker_info['header_header_stamp'] = m.header.stamp
		marker_info['namespace'] = m.ns
		marker_info['id'] = m.id
		marker_info['type'] = m.type
		marker_info['action'] = m.action
		marker_info['pose_position_x'] = m.pose.position.x
		marker_info['pose_position_y'] = m.pose.position.y
		marker_info['pose_position_z'] = m.pose.position.z
		marker_info['pose_orientation_x'] = m.pose.orientation.x
		marker_info['pose_orientation_y'] = m.pose.orientation.y
		marker_info['pose_orientation_z'] = m.pose.orientation.z
		marker_info['pose_orientation_w'] = m.pose.orientation.w


		markerarray_info.append(marker_info)

	pickle.dump(markerarray_info, output)



def listener():

	rospy.init_node("listener", anonymous=True)
	rospy.Subscriber("chair", MarkerArray, callback, queue_size=10)
	rospy.spin()


if __name__ == '__main__':
	listener()

