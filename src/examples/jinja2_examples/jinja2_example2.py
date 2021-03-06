#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # Example: Generate ROS2 components from a sp model
    # V.1.0.0.
#----------------------------------------------------------------------------------------------------------------------#

import sys
import os

# Specify package root
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Look for more modules
sys.path.append(root + "/src/jinja2")

from jinja2_generators.ros2_component_generator import ComponentGenerator
from jinja2 import Template, Environment, PackageLoader, FileSystemLoader

# sp_model (should actually collect it from all abilies connected to the resource, try to make another ability for backwards and set idle)

name = 'tool'
# lets say that we have 3 var types:
#	1. command only
#	2. a command and measured pair type
#	3. measured only
# might need some flag in the measured only variables like '_Q', so torque_reached_Q for instance, this is to help emulators fill in the effects in the
# transitions where they are not defined (hopefully it does not ruin the desired behavior...)

variables = ['set_idle', 'set_running_forw', 'idle', 'running_forw', 'torque_reached']

# updates format: [[name, [[current_values], [updated_values]], effects],
#                  [name, [[current_values], [updated_values]], effects],
#                  [name, [[current_values], [updated_values]], effects] and so on...]
#
# have to assert if all have _C or _M and if all of them are in variables

updates = [['enabled', [['idle', '!running_forw', 'set_idle', '!set_running_forw'], ['set_idle = False', 'set_running_forw = True']], []],
           ['starting', [['!set_idle', 'set_running_forw', '!running_forw'], []], ['idle = False', 'running_forw = True', 'torque_reached = False']],
           ['executing', [['!set_idle', 'set_running_forw', 'running_forw'], []], ['torque_reached = True']],
           ['finished', [['!set_idle', 'set_running_forw', 'torque_reached'], ['set_idle = True', 'set_running_forw = False']], []],
           ['resetting', [['set_idle', '!set_running_forw', 'running_forw'], []], ['idle = True', 'running_forw = False']]]

# lets say we know when it is untightened...
#variables = ['set_idle', 'set_running_forw', 'set_running_back', 'idle', 'running_forw', 'running_back', 'torque_reached', 'untightened']

# extended the model with backward running
# updates = [['enabledForw', [['idle', '!running_forw', '!running_back', 'set_idle', '!set_running_forw', '!set_running_back'], ['set_idle = False', 'set_running_forw = True']], []],
#            ['startingForw', [['!set_idle', 'set_running_forw', '!running_forw', '!running_back', '!set_running_back'], []], ['idle = False', 'running_forw = True']],
#            ['executingForw', [['!set_idle', 'set_running_forw', 'running_forw', '!running_back', '!set_running_back'], []], ['torque_reached = True']],
#            ['finishedForw', [['!set_idle', 'set_running_forw', 'torque_reached', '!running_back', '!set_running_back'], ['set_idle = True', 'set_running_forw = False']], []],
#            ['resettingForw', [['set_idle', '!set_running_forw', 'running_forw', '!running_back', '!set_running_back'], []], ['idle = True', 'running_forw = False']],
#            ['enabledBack', [['idle', '!running_forw', '!running_back', 'set_idle', '!set_running_forw', '!set_running_back'], ['set_idle = False', 'set_running_back = True']], []],
#            ['startingBack', [['!set_idle', '!set_running_forw', '!running_forw', '!running_back', 'set_running_back'], []], ['idle = False', 'running_back = True']],
#            ['executingBack', [['!set_idle', '!set_running_forw', '!running_forw', 'running_back', 'set_running_back'], []], ['untightened = True']],
#            ['finishedBack', [['!set_idle', '!set_running_forw', 'untightened', '!running_forw', 'set_running_back'], ['set_idle = True', 'set_running_back = False']], []],
#            ['resettingBack', [['set_idle', '!set_running_back', 'running_back', '!running_forw', '!set_running_forw'], []], ['idle = True', 'running_back = False']]]

c = ComponentGenerator()
c.sp_model_based_ros2_sp_emulator_node_gen(name, variables, updates)
c.sp_model_based_ros2_sp_interfacer_node_gen(name, variables, updates)
c.sp_model_based_ros2_node_tests_gen(name, variables, updates)
