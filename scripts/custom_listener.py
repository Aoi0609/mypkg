#!/usr/bin/env python3

import rospy
# from ros_practice_msgs.msg import Person
from mypkg.msg import Person

class Listener():
    def __init__(self):
        self.text_sub = rospy.Subscriber("/person", Person, self.callback)
    
    def callback(self, msg):
        name = msg.name
        age = msg.age
        hobbies = msg.hobbies
        
        hobbies = f"{hobbies[0]},{hobbies[1]}"
        
        rospy.loginfo(f"a,anataha...{name}、{age}sai!syumiha{hobbies}nanoka...")
        
if __name__ == "__main__":
    rospy.init_node("custom_listener_node")
    
    listener = Listener()
    rospy.spin()