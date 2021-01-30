#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range


class Robot:
    def __init__(self):
        self.sonar = 0 #Sonar distance

        '''Listener and publisher'''
        rospy.Subscriber("/sensor/sonar_front", Range, self.callbacksonar)
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

    def callbacksonar(self,data):
        self.sonar = data.range

    def get_sonar(self):
        return float(self.sonar)

    def set_speed_angle(self, linear_vel, angular_vel):
        cmd_vel = Twist()
        cmd_vel.linear.x = linear_vel
        cmd_vel.angular.z = angular_vel
        self.cmd_vel_pub.publish(cmd_vel)


def run_demo():
    '''Main loop'''
    robot = Robot()
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        #Write your strategy here ...
        linear_velocity = 0
        angular_velocity = 0
        sonar = robot.get_sonar()
        print("SONAR VALUE : {:.2f}".format(sonar))

        #Finishing by publishing the desired speed. DO NOT TOUCH.
        robot.set_speed_angle(linear_velocity, angular_velocity)
        rate.sleep()


if __name__ == "__main__":
    print("Running ROS..")
    rospy.init_node("Strategy", anonymous = True)

    run_demo()
