from supremica_components import Automata
from supremica_components import SynchronizationOptions
from supremica_components import AutomataSynchronizer

class Synchronizer:

    def make_options(self):
        # Using defaul options - might have to set full
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
        s = synced.make(auts, opts)
        s.execute()
        s.getAutomaton()

        return s2