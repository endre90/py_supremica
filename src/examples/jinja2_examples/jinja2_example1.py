#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # Example: Generate ROS2 components from an automaton
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
sys.path.append(root + "/src/jinja2")

from automata_generator import Generator
from automata_synchronizer import Synchronizer
from jinja2_generators.ros2_component_generator import ComponentGenerator
from jinja2 import Template, Environment, PackageLoader, FileSystemLoader

# Define the automaton
name = 'tool'
states = ['idle', 'running_forw', 'running_back', 'torque_reached']
alphabet = ['run_forw', 'run_back', 'set_idle', 'torque_tresh']
u_alphabet = ['torque_tresh']
arcs = [('t1', 'idle', 'running_forw', 'run_forw'),
        ('t2', 'running_forw', 'torque_reached', 'torque_tresh'),
        ('t3', 'running_forw', 'idle', 'set_idle'),
        ('t4', 'torque_reached', 'idle', 'set_idle'),
        ('t5', 'idle', 'running_back', 'run_back'),
        ('t6', 'running_back', 'idle', 'set_idle')]
init = 'idle'
marked = ['idle']
forbidden = []   

# Generate automaton
g = Generator()
aut1 = g.generate_automaton(name, states, alphabet, u_alphabet, arcs, init, marked, forbidden)

# Generate ROS2 node
c = ComponentGenerator()
c.automaton_based_ros2_node_gen(aut1)

# Generate ROS2 messages
c.automaton_based_ros2_msg_gen(aut1)