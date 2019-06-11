#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # Automata synchronizer using Supremica classes via supremica_components
    # V.1.0.0.
#----------------------------------------------------------------------------------------------------------------------#

import sys
import os

# Specify package root
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Look for more modules
sys.path.append(root + "/src/generators")
sys.path.append(root + "/src/components")
sys.path.append(root + "/src/algorithms")

from supremica_components import Automata
from supremica_components import SynchronizationType
from supremica_components import SynchronizationOptions
from supremica_components import AutomataSynchronizer

class Synchronizer:

    def make_options(self, s_type):
        opt = SynchronizationOptions()
        opt1 = opt.make()
        opt1.setSynchronizationType(self.make_type(s_type))
        return opt1
    
    def make_type(self, s_type):
        synch_type = SynchronizationType()
        synch_type_1 = synch_type.make()

        if s_type == "PRIORITIZED":
            return synch_type_1.PRIORITIZED
        elif s_type == "FULL":
            return synch_type_1.FULL
        elif s_type == "BROADCAST":
            return synch_type_1.BROADCAST
        else:
            raise TypeError("Non valid syncronization type: " + s_type)

    def make_automata(self, automata):

        aut = Automata()
        aut1 = aut.make()
        for a in automata:
            aut1.addAutomaton(a)
        return aut1

    def synchronize_automata(self, automata, s_type):

        if not isinstance(automata, list):
            raise TypeError("Argument automata must be of type List.")
        if not isinstance(s_type, str):
            raise TypeError("Argument s_type must be of type String.")

        auts = self.make_automata(automata)
        opts = self.make_options(s_type)

        synced = AutomataSynchronizer()
        s = synced.make(auts, opts)
        s.execute()
        s2 = s.getAutomaton()

        return s2