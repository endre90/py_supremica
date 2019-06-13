#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # Autogenerated ROS2 emulator using jinja2
    # V.1.0.0.
#----------------------------------------------------------------------------------------------------------------------#

import sys
import rclpy
import time
from {{ package_name }} import {{ message_type_driver_to_emulator }}
from {{ package_name }} import {{ message_type_emulator_to_driver }}

class {{ resource_name }}_sp_emulator():

    def __init__(self, args=None):

        rclpy.init(args=args)

        self.node = rclpy.create_node("{{ resource_name }}_sp_emulator")
        self.msg_emulator_to_driver = {{ message_type_emulator_to_driver }}()
        self.msg_driver_to_emulator = {{ message_type_driver_to_emulator }}()
        {% for item in states %}
        self.{{ item }} = 0
        {%- endfor %}
        {% for item in commands %}
        self.{{ item }} = 0
        {%- endfor %}
        {% for item in replies %}
        self.{{ item }} = 0
        {%- endfor %}

        self.timer_period = 0.1

        self.{{ resource_name }}_emulator_sub = self.node.create_subscription({{ message_type_driver_to_emulator }}, 
                                                                        "/{{ resource_name }}_driver_to_emulator", 
                                                                        self.{{ resource_name }}_driver_to_emulator_callback)
        self.{{ resource_name }}_emulator_pub = self.node.create_publisher({{ message_type_emulator_to_driver }}, 
                                                                        "/{{ resource_name }}_emulator_to_driver")
        self.publisher_tmr = self.node.create_timer(self.timer_period, self.timer_callback)
        self.main_tmr = self.node.create_timer(self.timer_period, self.main_callback)

        rclpy.spin(self.node)
        self.node.destroy_node()
        rclpy.shutdown()
    

    def timer_callback(self):
        {% for item in states %}
        self.msg_emulator_to_driver.{{ item }} = self.{{ item }}
        {%- endfor %}

        self.pub.publish(self.msg_emulator_to_driver)


    def {{ resource_name }}_driver_to_emulator_callback(self, data):
        {% for item in commands %}
        self.{{ item }} = data.{{ item }}
        {%- endfor %}
        {% for item in commands %}
        if self.{{ item }} == 1:
        # Do something here
        {%- endfor %}


    def main_callback(self):
        {% for item in replies %}
        # have to send an {{ item }} event back to SP in the state msg
        # or keep state in the node istelf and update just the "torque_reached" line?
        {%- endfor %}
        {% for item in states %}
        # collect the {{ item }} state here
        {%- endfor %}

        # define stuff here manually

if __name__ == '__main__':
    {{ resource_name }}_emulator()
