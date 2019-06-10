#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # Automata generator using Supremica classes via supremica_components
    # V.1.0.0.
#----------------------------------------------------------------------------------------------------------------------#

from supremica_components import State
from supremica_components import LabeledEvent
from supremica_components import Arc
from supremica_components import Alphabet
from supremica_components import Automaton

class Generator():

    # The new lambdas:
    def make_event(self, x, u_alphabet):
        e = LabeledEvent()
        if x in u_alphabet:
            return self.set_uncontrollable(e.make(x))
        else:
            return self.set_controllable(e.make(x))

    def make_state(self, x, init, marked, forbidden):
        s = State()
        if x == init:
            return self.set_initial(s.make(x))
        elif x in marked:
            return self.set_marked(s.make(x))
        elif x in forbidden:
            return self.set_forbidden(s.make(x))
        else:
            return s.make(x)
    
    def set_controllable(self, x):
        x.setControllable(True)
        return x

    def set_uncontrollable(self, x):
        x.setControllable(False)
        return x

    def set_initial(self, x):
        x.setInitial(True)
        return x
    
    def set_marked(self, x):
        x.setAccepting(True)
        return x
    
    def set_forbidden(self, x):
        x.setForbidden(True)
        return x

    def make_arc(self, source, sink, event):
        a = Arc()
        return a.make(source, sink, event)

    # Not used currently(alph is alph of aut):
    # def make_alphabet(self, alphabet, u_alphabet):
        # alph = Alphabet()
        # alph_1 = alph.make()

        # for e in alphabet:
            # if '!' in e:
                # alph_1.addEvent(self.set_uncontrollable(self.make_event(e)))
            # else:
                # alph_1.addEvent(self.set_controllable(self.make_event(e)))
        # 
        # return alph_1

    def make_automaton(self, name, states, alphabet, u_alphabet, arcs, init, marked, forbidden):
    
        if "state" in states or "arc" in arcs or "event" in alphabet:
            raise TypeError("invalid state, event or arc name.")

        for state in states:
            exec('{} = self.make_state({}, init, marked, forbidden)'.format(state, ('"{}"'.format(state))))
        
        for event in alphabet:
            exec('{} = self.make_event({}, u_alphabet)'.format(event, ('"{}"'.format(event))))

        for arc in arcs:
            exec('{} = self.make_arc({}, {}, {})'.format(arc[0], arc[1], arc[2], arc[3]))
        
        # Not used currently(alph is alph of aut):
        # alph = self.make_alphabet(alphabet)
    
        aut = Automaton()
        aut_1 = aut.make(name)

        for state in states:
            aut_1.addState(eval(state))

        for arc in arcs:
            aut_1.addArc(eval(arc[0]))

        for event in alphabet:
            aut_1.getAlphabet().addEvent(eval(event))

        return aut_1
    

    def generate_automaton(self, name, states, alphabet, u_alphabet, arcs, init, marked, forbidden):

        if not isinstance(name, str):
            raise TypeError("Argument name must be of type String.")

        if not isinstance(states, list):
            raise TypeError("Argument states must be of type List.")
        for state in states:
            if not isinstance(state, str):
                raise TypeError("Argument element of states must be of type String.")

        if not isinstance(alphabet, list):
            raise TypeError("Argument alphabet must be of type List.")
        for event in alphabet:
            if not isinstance(event, str):
                raise TypeError("Argument element of alphabet must be of type String.")
        
        if not isinstance(arcs, list):
            raise TypeError("Argument arcs must be of type List.")
        for arc in arcs:
            if not isinstance(arc, tuple):
                raise TypeError("Argument element of arcs must be of type Tuple.")
            for elem in arc:
                if not isinstance(elem, str):
                    raise TypeError("Element of argument element of arcs must be of type String.")
            if not isinstance(arc[0], str):
                raise TypeError("Argument element 'arc name' a.k.a. arc[0] must be of type String.")
            if not arc[1] in states:
                raise TypeError("Source state must be in states.")
            if not arc[2] in states:
                raise TypeError("Sink state must be in states.")
            if not arc[3] in alphabet:
                raise TypeError("Event that labels the arc must be in alphabet.")

        if not isinstance(init, str):
            raise TypeError("Argument init must be of type String.")
        if not init in states:
            raise TypeError("Initial state must be in states.")

        if not isinstance(marked, list):
            raise TypeError("Argument marked must be of type List.")
        for mark in marked:
            if not isinstance(mark, str):
                raise TypeError("Argument element of marked must be of type String.")
            if not mark in states:
                raise TypeError("Marked state " + mark + " must be in states.")
        
        if not isinstance(forbidden, list):
            raise TypeError("Argument forbidden must be of type List.")
        for forb in forbidden:
            if not isinstance(forb, str):
                raise TypeError("Argument element of forbidden must be of type String.")
            if not forb in states:
                raise TypeError("Forbidden state " + forb + " must be in states.")

        return self.make_automaton(name, states, alphabet, u_alphabet, arcs, init, marked, forbidden)        