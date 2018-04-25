
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import pickle
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker


def movebase_client():

    client = actionlib.SimpleActionClient('move_base_navi',MoveBaseAction)
    print('creat')
    client.wait_for_server()
    print('wait for server')
    # t = tflistener.getLatestCommonTime("/base_link", "/map")
    # robot_position, quaternion = tflistener.lookupTransform("/base_link", "/map", t)


    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time(0)
    # print(markerArray.markers[0].pose.position.x, markerArray.markers[0].pose.position.y)
    goal.target_pose.pose.position.x = markerArray.markers[0].pose.position.x
    goal.target_pose.pose.position.y = markerArray.markers[0].pose.position.y
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    print('sent goal and wait')
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

def listener():
    rospy.init_node("talker", anonymous=True)
    global pub
    global markerArray
    pub = rospy.Publisher('chair', MarkerArray, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(markerArray)
        rate.sleep()


if __name__ == '__main__':

    #load_chair_info first
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
        # print(marker.pose.position.x, marker.pose.position.y)
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

    # listener()

    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")