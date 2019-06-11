import sys
import rclpy
import time
from ros_autogen_testing import tool_sp_to_driver
from ros_autogen_testing import tool_driver_to_sp

class tool_sp_driver():

    def __init__(self, args=None):

        rclpy.init(args=args)

        self.node = rclpy.create_node("tool_sp_driver")
        self.msg_sp_to_driver = tool_sp_to_driver()
        self.msg_driver_to_sp = tool_driver_to_sp()
        
        self.idle = 0
        self.running_forw = 0
        self.running_back = 0
        self.torque_reached = 0
        
        self.run_forw = 0
        self.run_back = 0
        self.set_idle = 0
        self.torque_tresh = 0
        self.finish = 0

        self.timer_period = 0.1

        self.tool_sp_sub = self.node.create_subscription(tool_sp_to_driver, "/tool_sp_to_driver", self.tool_sp_to_driver_callback)
        self.tool_sp_pub = self.node.create_publisher(tool_driver_to_sp, "/tool_driver_to_sp")
        self.publisher_tmr = self.node.create_timer(self.timer_period, self.timer_callback)
        self.main_tmr = self.node.create_timer(self.timer_period, self.main_callback)

        rclpy.spin(self.node)
        self.node.destroy_node()
        rclpy.shutdown()
    

    def timer_callback(self):
        
        self.msg_driver_to_sp.idle = self.idle
        self.msg_driver_to_sp.running_forw = self.running_forw
        self.msg_driver_to_sp.running_back = self.running_back
        self.msg_driver_to_sp.torque_reached = self.torque_reached

        self.pub.publish(self.msg_driver_to_sp)


    def tool_sp_to_driver_callback(self, data):
        
        if self.data.run_forw == 1:
            # Do something here
        if self.data.run_back == 1:
            # Do something here
        if self.data.set_idle == 1:
            # Do something here
        if self.data.torque_tresh == 1:
            # Do something here
        if self.data.finish == 1:
            # Do something here


    def main_callback(self):
        
        # collect the idle state here
        # collect the running_forw state here
        # collect the running_back state here
        # collect the torque_reached state here

        # define stuff here manually

if __name__ == '__main__':
    tool_sp_driver()