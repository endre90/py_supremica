import sys
import rclpy
import time
from {{ package_name }} import {{ message_type_sp_to_driver }}
from {{ package_name }} import {{ message_type_driver_to_sp }}

class {{ resource_name }}_sp_driver():

    def __init__(self, args=None):

        rclpy.init(args=args)

        self.node = rclpy.create_node("{{ resource_name }}_sp_driver")
        self.msg_sp_to_driver = {{ message_type_sp_to_driver }}()
        self.msg_driver_to_sp = {{ message_type_driver_to_sp }}()
        {% for item in states %}
        self.{{ item }} = 0
        {%- endfor %}
        {% for item in commands %}
        self.{{ item }} = 0
        {%- endfor %}

        self.timer_period = 0.1

        self.{{ resource_name }}_sp_sub = self.node.create_subscription({{ message_type_sp_to_driver }}, "/{{ resource_name }}_sp_to_driver", self.{{ resource_name }}_sp_to_driver_callback)
        self.{{ resource_name }}_sp_pub = self.node.create_publisher({{ message_type_driver_to_sp }}, "/{{ resource_name }}_driver_to_sp")
        self.publisher_tmr = self.node.create_timer(self.timer_period, self.timer_callback)
        self.main_tmr = self.node.create_timer(self.timer_period, self.main_callback)

        rclpy.spin(self.node)
        self.node.destroy_node()
        rclpy.shutdown()
    

    def timer_callback(self):
        {% for item in states %}
        self.msg_driver_to_sp.{{ item }} = self.{{ item }}
        {%- endfor %}

        self.pub.publish(self.msg_driver_to_sp)


    def {{ resource_name }}_sp_to_driver_callback(self, data):
        {% for item in commands %}
        if self.data.{{ item }} == 1:
            # Do something here
        {%- endfor %}


    def main_callback(self):
        {% for item in states %}
        # collect the {{ item }} state here
        {%- endfor %}

        # define stuff here manually

if __name__ == '__main__':
    {{ resource_name }}_sp_driver()
