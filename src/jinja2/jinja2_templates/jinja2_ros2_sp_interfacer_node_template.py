#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # Autogenerated ROS2 {{ resource_name }} interfacer node using jinja2
    # V.1.0.0.
#----------------------------------------------------------------------------------------------------------------------#

import sys
import rclpy
import time
from {{ package_name }}.msg import {{ message_type_sp_to_interfacer }}
from {{ package_name }}.msg import {{ message_type_interfacer_to_sp }}
from {{ package_name }}.msg import {{ message_type_driver_to_interfacer }}
from {{ package_name }}.msg import {{ message_type_interfacer_to_driver }}

class {{ resource_name }}_sp_interfacer():

    def __init__(self, args=None):

        rclpy.init(args=args)

        self.node = rclpy.create_node("{{ resource_name }}_sp_interfacer")
        self.msg_sp_to_interfacer = {{ message_type_sp_to_interfacer }}()
        self.msg_interfacer_to_sp = {{ message_type_interfacer_to_sp }}()
        self.msg_driver_to_interfacer = {{ message_type_driver_to_interfacer }}()
        self.msg_interfacer_to_driver = {{ message_type_interfacer_to_driver }}()
        {% for item in measured_variables %}
        self.{{ item }} = False
        {%- endfor %}
        {% for item in command_variables %}
        self.{{ item }} = False
        {%- endfor %}

        self.{{ resource_name }}_sp_sub = self.node.create_subscription({{ message_type_sp_to_interfacer }}, 
                                                                        "/{{ resource_name }}_sp_to_interfacer", 
                                                                        self.{{ resource_name }}_sp_to_interfacer_callback)
        self.{{ resource_name }}_sp_pub = self.node.create_publisher({{ message_type_interfacer_to_sp }}, 
                                                                        "/{{ resource_name }}_interfacer_to_sp")
        self.{{ resource_name }}_driver_sub = self.node.create_subscription({{ message_type_driver_to_interfacer }}, 
                                                                        "/{{ resource_name }}_driver_to_interfacer", 
                                                                        self.{{ resource_name }}_driver_to_interfacer_callback)
        self.{{ resource_name }}_driver_pub = self.node.create_publisher({{ message_type_interfacer_to_driver }}, 
                                                                        "/{{ resource_name }}_interfacer_to_driver")

        rclpy.spin(self.node)
        self.node.destroy_node()
        rclpy.shutdown()
    
    # Just forwarding from sp to one of the lower nodes based on the launch spec
    def {{ resource_name }}_sp_to_interfacer_callback(self, data):
        {% for item in command_variables %}
        self.{{ item }} = data.{{ item }}
        self.msg_interfacer_to_driver.{{ item }} = self.{{ item }}
        {%- endfor %}
        self.{{ resource_name }}_driver_pub.publish(self.msg_interfacer_to_driver)

    # Just forwarding from one of the lower nodes to to based on the launch spec
    def {{ resource_name }}_driver_to_interfacer_callback(self, data):
        {% for item in measured_variables %}
        self.{{ item }} = data.{{ item }}
        self.msg_interfacer_to_sp.{{ item }} = self.{{ item }}
        {%- endfor %}
        {% for item in command_variables %}
        self.msg_interfacer_to_sp.got_{{ item }} = self.{{ item }}
        {%- endfor %}

        self.{{ resource_name }}_sp_pub.publish(self.msg_interfacer_to_sp)

if __name__ == '__main__':
    {{ resource_name }}_sp_interfacer()