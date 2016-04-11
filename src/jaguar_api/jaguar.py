#!/usr/bin/ipython -i

from robot_api.robot import Robot
from robot_api.parts import Arm, Base

import rospy

class Jaguar(Robot):

    def __init__(self):
        super(self.__class__, self).__init__("jaguar")
        self.add_part(Arm, "arm")
        self.add_part(Base, "base")

if __name__ == "__main__":
    rospy.init_node("robot_api", anonymous=True)
    j = Jaguar()
    print "\033[1;33m--------------------------------\n| Jaguar console - version 0.1 |\n--------------------------------\033[1;m"
    print "\033[92m Use the Jaguar Object (j) to interact with the Jaguar robot.\033[1;m"
