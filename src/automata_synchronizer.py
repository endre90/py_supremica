from components import Automata
from components import SynchronizationOptions
from components import AutomataSynchronizer

class Synchronizer:

    def make_options(self):
        opt = SynchronizationOptions()
        opt1 = opt.make()
        return opt1

    def make_automata(self, automata):

        aut = Automata()
        aut1 = aut.make()
        for a in automata:
            aut1.addAutomaton(a)
        return aut1

    def synchronize_automata(self, automata):

        if not isinstance(automata, list):
            raise TypeError("Argument automata must be of type List.")

        auts = self.make_automata(automata)
        print(auts)
        opts = self.make_options()

        synced = AutomataSynchronizer()
        s = synced.make(auts)
        
        return s
