from components import State
from components import LabeledEvent
from components import Arc
from components import Alphabet
from components import Automaton

class Generator():

    def make_event(self, x):
        e = LabeledEvent()
        return e.make(x)

    def make_state(self, x):
        s = State()
        return s.make(x)
    
    def set_controllable(self, x):
        x.setControllable(True)
        return x

    def set_uncontrollable(self, x):
        x.setControllable(False)
        return x

    def make_arc(self, source, sink, event):
        a = Arc()
        return a.make(source, sink, event)

    def make_alphabet(self, alphabet):
        alph = Alphabet()
        alph_1 = alph.make()

        for e in alphabet:
            if '!' in e:
                alph_1.addEvent(self.set_uncontrollable(self.make_event(e)))
            else:
                alph_1.addEvent(self.set_controllable(self.make_event(e)))
        
        return alph_1

    def make_automaton(self, name, alphabet, states, arcs):
        aut = Automaton()
        aut_1 = aut.make(name, self.make_alphabet(alphabet))
        print(aut_1.getEvents()) #not workin

        for state in states:
            aut_1.addState(self.make_state(state))
        
        print(aut_1.getStates())
        
        for arc in arcs:
            aut_1.addArc(self.make_arc(self.make_state(arc[0]), 
                                       self.make_state(arc[1]),
                                       self.make_event(arc[2])))
            print(arc)

        return aut_1
    
    def generate_automaton(self, name, alphabet, states, arcs):
        if not isinstance(name, str):
            raise TypeError("Argument name must be of type String.")

        if not isinstance(alphabet, list):
            raise TypeError("Argument alphabet must be of type List.")
        for event in alphabet:
            if not isinstance(event, str):
                raise TypeError("Argument element of alphabet must be of type String.")
        
        if not isinstance(states, list):
            raise TypeError("Argument states must be of type List.")
        for state in states:
            if not isinstance(state, str):
                raise TypeError("Argument element of states must be of type String.")
        
        if not isinstance(arcs, list):
            raise TypeError("Argument arcs must be of type List.")
        for arc in arcs:
            if not isinstance(arc, tuple):
                raise TypeError("Argument element of arcs must be of type Tuple.")
            for elem in arc:
                if not isinstance(elem, str):
                    raise TypeError("Element of argument element of arcs must be of type String.")
            if not arc[0] in states:
                raise TypeError("Source state must be in states")
            if not arc[1] in states:
                raise TypeError("Sink state must be in states")
            if not arc[2] in alphabet:
                raise TypeError("Event that labels the arc must be in alphabet")
            
        return self.make_automaton(name, alphabet, states, arcs)