
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
from std_msgs.msg import Int32
from visualization_msgs.msg import Marker

 
done = False

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
    robot_position, quaternion = tflistener.lookupTransform("/base_link", "/map", rospy.Time(0))
    robot_position = [-p for p in robot_position]
    
    print('robot position before: ', robot_position)
    goal_x, goal_y = find_closet_chair(robot_position)
    
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "/map"
    goal.target_pose.header.stamp = rospy.Time(0)
    if(goal_x < 0):
        goal.target_pose.pose.position.x = goal_x+0.5
    else:
        goal.target_pose.pose.position.x = goal_x-0.5
    if(goal_y < 0):
        goal.target_pose.pose.position.y = goal_y+0.5
    else:
        goal.target_pose.pose.position.y = goal_y-0.5
    goal.target_pose.pose.orientation.w = 1.0

    print('goal location: ', goal_x, goal_y)

    marker = Marker()
    marker.header.frame_id = "map"
    marker.header.stamp = rospy.get_rostime()
    marker.ns = "my_namespace"
    marker.id = 0
    marker.type = marker.SPHERE
    marker.action = marker.ADD
    marker.pose.position.x = goal_x
    marker.pose.position.y = goal_y
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = 0.3
    marker.scale.y = 0.3
    marker.scale.z = 0.3
    marker.color.a = 1.0 
    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0
    marker.mesh_resource = "package://pr2_description/meshes/base_v0/base.dae"
   
    global pub
    pub.publish(marker)

    client.send_goal(goal)
    print('sent goal and wait')
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

def finite_state_machine(data):
    print("received data: ", data.data)
    if data.data == 0 or done:
        #INIT STATE, DO NOTHING
        return
    else:
        #NAVIGATION STATE
        print("people detected")
        soundhandle.say("Please wait to be seated")
        rospy.sleep(5)
        try:
            result = movebase_client()
            print("execution result: ", result)
            tflistener.waitForTransform("/base_link", "/map", rospy.Time(0), rospy.Duration(4.0))
            robot_position, quaternion = tflistener.lookupTransform("/base_link", "/map", rospy.Time(0))
            robot_position = [-p for p in robot_position]
            print('robot position after: ', robot_position)
            global done
            done = True
            if result:
                rospy.loginfo("Goal execution done!")
                soundhandle.say("Here is your seat sir")
        except rospy.ROSInterruptException:
            rospy.loginfo("Navigation test finished.")


def callback(data):
    print(data)
    finite_state_machine(data)


def listener():
    rospy.Subscriber("/person", Int32, callback, queue_size=10)
    global pub 
    pub = rospy.Publisher('goal', Marker, queue_size=10)
    rospy.spin()


if __name__ == '__main__':

    #load_chair_info first
    global chair_info
    with open('chair_info.pkl', 'rb') as f:
        chair_info = pickle.load(f)
    print(len(chair_info))

    global tflistener
    tflistener = TransformListener()

    rospy.init_node('nav')
    print("say hello")
    global soundhandle
    soundhandle = SoundClient()
    rospy.sleep(1)
    soundhandle.say('hello')

    listener()

