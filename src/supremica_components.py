#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # Python access for Supremica Java classes
    # V.1.0.0.
#----------------------------------------------------------------------------------------------------------------------#

import jpype

# Specify your .jar paths
CLASSPATH = """/home/endre/Supremica/dist/Supremica.jar:
               /home/endre/Supremica/dist/SupremicaLib.jar:
               /home/endre/Supremica/dist/SupremicaTest.jar"""

jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % CLASSPATH)

# Automata generation classes
STATE = jpype.JPackage("org").supremica.automata.State
STATESET = jpype.JPackage("org").supremica.automata.StateSet
LABELEDEVENT = jpype.JPackage("org").supremica.automata.LabeledEvent
ALPHABET = jpype.JPackage("org").supremica.automata.Alphabet
ARC = jpype.JPackage("org").supremica.automata.Arc
AUTOMATON = jpype.JPackage("org").supremica.automata.Automaton
AUTOMATA = jpype.JPackage("org").supremica.automata.Automata

# Syncronization classes
SYNCHRONIZATIONTYPE = jpype.JPackage("org").supremica.automata.algorithms.SynchronizationType
SYNCHRONIZATIONOPTIONS = jpype.JPackage("org").supremica.automata.algorithms.SynchronizationOptions
AUTOMATASYNCHRONIZER = jpype.JPackage("org").supremica.automata.algorithms.AutomataSynchronizer


class State:

    def make(self, name):

        if not isinstance(name, str):
            raise TypeError("Argument name must be of type String.")

        s = STATE(name)
    
        return s


class Alphabet:

    def make(self):

        alph = ALPHABET() 

        return alph

    
class LabeledEvent:

    def make(self, name):

        if not isinstance(name, str):
            raise TypeError("Argument name must be of type String.")
        
        e = LABELEDEVENT(name)
    
        return e


class Arc:

    def make(self, fromState, toState, event):

        args = [fromState, toState, event]

        if not isinstance(fromState, STATE):
            raise TypeError("Argument fromState must be of type components.State.")
        if not isinstance(toState, STATE):
            raise TypeError("Argument toState must be of type components.State.")
        if not isinstance(event, LABELEDEVENT):
            raise TypeError("Argument event must be of type components.LabeledEvent.")

        arc = ARC(fromState, toState, event)

        return arc


class Automaton:

    def make(self, name):

        aut = AUTOMATON(name)

        return aut


class Automata:

    def make(self):

        aut = AUTOMATA()

        return aut


class SynchronizationOptions():

    def make(self):

        opt = SYNCHRONIZATIONOPTIONS()

        return opt


class SynchronizationType():

    def make(self):

        stype = SYNCHRONIZATIONTYPE

        return stype


class AutomataSynchronizer:

    def make(self, automata, options):

        aut = AUTOMATASYNCHRONIZER(automata, options)

        return aut