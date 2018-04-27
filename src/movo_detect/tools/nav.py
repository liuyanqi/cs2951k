
import rospy
import actionlib
import math
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import pickle
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from tf import TransformListener 
from thread import start_new_thread
from sound_play.libsoundplay import SoundClient


def find_closet_chair(robot_position):
    min_distance = 100
    minimum_req = 1
    min_idx = 0

    for idx, chair in enumerate(chair_info):

        distance = (robot_position[0] - chair_info[idx]['pose_position_x'])**2 + (robot_position[1] - chair_info[idx]['pose_position_y'])**2
        distance = math.sqrt(distance)

        if distance < min_distance and distance > minimum_req:
            min_distance = distance
            min_idx = idx

    return (chair_info[min_idx]['pose_position_x'], chair_info[min_idx]['pose_position_y'])


def movebase_client():

    client = actionlib.SimpleActionClient('move_base_navi',MoveBaseAction)
    print('creat')
    client.wait_for_server()
    print('wait for server')
    global tflistener
    tflistener.waitForTransform("/base_link", "/map", rospy.Time(0), rospy.Duration(4.0))
    # t = tflistener.getLatestCommonTime("/base_link", "/map")
    robot_position, quaternion = tflistener.lookupTransform("/base_link", "/map", rospy.Time(0))
    robot_position = [-p for p in robot_position]
    
    print(robot_position)
    goal_x, goal_y = find_closet_chair(robot_position)
    print(goal_x, goal_y)
    
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time(0)
    goal.target_pose.pose.position.x = goal_x
    goal.target_pose.pose.position.y = goal_y
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    print('sent goal and wait')
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

def finite_state_machine(data):
    if data == 0:
        #INIT STATE, DO NOTHING
        return
    else:
        #NAVIGATION STATE
        soundhandle.say("Please wait to be seated")
        rospy.sleep(5)
        try:
            result = movebase_client()
            if result:
                rospy.loginfo("Goal execution done!")
                soundhandle.say("Here is your sit sir")
        except rospy.ROSInterruptException:
            rospy.loginfo("Navigation test finished.")


def callback(data):
    print(data)

    finte_state_machine(data)


def listener():
    rospy.Subscriber("/person", Int32, callback, queue_size=10)


if __name__ == '__main__':

    #load_chair_info first
    global chair_info
    global markerArray
    markerArray = MarkerArray()
    with open('chair_info.pkl', 'rb') as f:
        chair_info = pickle.load(f)
    print(len(chair_info))

    rospy.init_node('nav')

    global soundhandle
    soundhandle = SoundClient()
    rospy.sleep(1)
    soundhandle.say('hello')

