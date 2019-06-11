#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # Example: Generate two automata and synch them
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

# Define automata
states1 = ['s1', 's2', 's3']
states2 = ['s1', 's2', 's3']
alphabet1 = ['e1', 'e2']
alphabet2 = ['e1', 'e3']
u_alphabet1 = []
u_alphabet2 = []
arcs1 = [('t1', 's1', 's2', 'e1'), ('t2', 's2', 's3', 'e2')]
arcs2 = [('t1', 's1', 's2', 'e1'), ('t4', 's2', 's3', 'e3')]
init1 = 's1'
init2 = 's1'
marked1 = ['s3']
marked2 = ['s3']
forbidden1 = []
forbidden2 = []

# Generate automata
g = Generator()
aut1 = g.generate_automaton('aut1', states1, alphabet1, u_alphabet1, arcs1, init1, marked1, forbidden1)
aut2 = g.generate_automaton('aut2', states2, alphabet2, u_alphabet2, arcs2, init2, marked2, forbidden2)

# Synchronize automata
s = Synchronizer()
auts = s.synchronize_automata([aut1, aut2], "FULL")
print(auts.getStates())
print(auts.getTransitions())
print(auts.getName())
