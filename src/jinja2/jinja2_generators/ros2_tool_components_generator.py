#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # ROS2 component generator
    # V.1.0.0.
#----------------------------------------------------------------------------------------------------------------------#

import sys
import os

# Specify package root
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Look for more modules
sys.path.append(root + "/src/generators")
sys.path.append(root + "/src/components")
sys.path.append(root + "/src/algorithms")

from automata_generator import Generator
from automata_synchronizer import Synchronizer
from jinja2 import Template, Environment, PackageLoader, FileSystemLoader

# Define automata
what = 'tool'
states = ['idle', 'running_forw', 'running_back', 'torque_reached']
alphabet = ['run_forw', 'run_back', 'set_idle', 'torque_tresh', 'finish']
u_alphabet = ['torque_tresh', 'finish']
arcs = [('t1', 'idle', 'running_forw', 'run_forw'),
        ('t2', 'running_forw', 'torque_reached', 'torque_tresh'),
        ('t3', 'running_forw', 'idle', 'set_idle'),
        ('t4', 'torque_reached', 'idle', 'finish'),
        ('t5', 'idle', 'running_back', 'run_back'),
        ('t6', 'running_back', 'idle', 'set_idle')]
init = 'idle'
marked = ['idle']
forbidden = []   

# Generate automata
g = Generator()
aut1 = g.generate_automaton('aut1', states, alphabet, u_alphabet, arcs, init, marked, forbidden)

templates_dir = os.path.join(root, 'src', 'jinja2', 'jinja2_templates')
env = Environment(loader = FileSystemLoader(templates_dir))

node_template = env.get_template('jinja2_ros2_node_template.py')
sp_to_driver_msg_template = env.get_template('jinja2_ros2_msg_template_sp_to_driver.msg')
driver_to_sp_msg_template = env.get_template('jinja2_ros2_msg_template_driver_to_sp.msg')

node_filename = os.path.join(root, 'src', 'jinja2', 'jinja2_autogenerated', 'ros2_nodes', '{}_sp_driver.py'.format(what))
sp_to_driver_msg_filename = os.path.join(root, 'src', 'jinja2', 'jinja2_autogenerated', 'ros2_messages', '{}_sp_to_driver.msg'.format(what))
driver_to_sp_msg_filename = os.path.join(root, 'src', 'jinja2', 'jinja2_autogenerated', 'ros2_messages', '{}_driver_to_sp.msg'.format(what))

# Generate ROS2 node
with open(node_filename, 'w') as fh:
    fh.write(node_template.render(
        resource_name = what,
        package_name = "ros_autogen_testing",
        message_type_sp_to_driver = '{}_sp_to_driver'.format(what),
        message_type_driver_to_sp = '{}_driver_to_sp'.format(what),
        states = states,
        commands = alphabet,
    ))

# Generate message
with open(sp_to_driver_msg_filename, 'w') as fh:
    fh.write(sp_to_driver_msg_template.render(
        commands = alphabet,
    ))

# Generate message
with open(driver_to_sp_msg_filename, 'w') as fh:
    fh.write(driver_to_sp_msg_template.render(
        commands = alphabet,
        states = states,
    ))
