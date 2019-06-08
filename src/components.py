#----------------------------------------------------------------------------------------------------------------------#
# authors, description, version
#----------------------------------------------------------------------------------------------------------------------#
    # Endre Er{\H o}s
    # Python port for Supremica Java classes
    # V.0.0.1

    # Ported classes: State, LabeledEvent, ARc
#----------------------------------------------------------------------------------------------------------------------#

import jpype

CLASSPATH = "/home/endre/Supremica/dist/Supremica.jar:/home/endre/Supremica/dist/SupremicaLib.jar:/home/endre/Supremica/dist/SupremicaTest.jar"
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % CLASSPATH)

STATE = jpype.JPackage("org").supremica.automata.State
STATESET = jpype.JPackage("org").supremica.automata.StateSet
LABELEDEVENT = jpype.JPackage("org").supremica.automata.LabeledEvent
ALPHABET = jpype.JPackage("org").supremica.automata.Alphabet
ARC = jpype.JPackage("org").supremica.automata.Arc
AUTOMATON = jpype.JPackage("org").supremica.automata.Automaton


class State:

    def make(self, name):

        if not isinstance(name, str):
            raise TypeError("Argument name must be of type String.")

        s = STATE(name)
    
        return s


class Alphabet:

    # JAVA API: size, nbrOfEvents, iterator, controllableEventIterator,
    #           uncontrollableEventIterator, addEvent, addEvents, removeEvent,
    #           contains, getEvents, nbrOfControllableEvents, nbrOfUncontrollableEvents,
    #           nbrOfUnobservableEvents, getUnobservableEvents, nbrOfPrioritizedEvents,
    #           nbrOfImmediateEvents, toDebugString, toString, values...

    def make(self):

        alph = ALPHABET() 

        return alph

    
class LabeledEvent:

    # JAVA API: clone, toString, getLabel, isControllable, setControllable, 
    #           isObservable, setObservable, isOperatorIncrease, setOperatorIncrease,
    #           isOperatorReset, setOperatorReset, isImmediate, setImmediate, 
    #           isPrioritized, setPrioritized, isUnobservable, setUnobservable,
    #           isProposition, setProposition, setExpansionPriority, 
    #           getExpansionPriority, equals, hashCode, getIndex, setIndex,
    #           compareTo, idForbidden, isTauEvent, getProxyInterface, refequals,
    #           refHashCode, acceptVisitor, getName, getKind, getAttributes

    def make(self, name):

        if not isinstance(name, str):
            raise TypeError("Argument name must be of type String.")
        
        e = LABELEDEVENT(name)
    
        return e


class Arc():

    # JAVA API: clone, getEvent, getToState, getTarget, getFromState, getSource,
    #           getLabel, isSelfLoop, clear, equals, hashCode, toString, compareTo,
    #           compare, getProxyInterface, acceptVisitor, setProbability, getProbability

    def make(self, fromState, toState, event):

        args = [fromState, toState, event]

        #if not isinstance(name, str):
        #    raise TypeError("Argument name must be of type String.")
        if not isinstance(fromState, STATE):
            raise TypeError("Argument fromState must be of type components.State.")
        if not isinstance(toState, STATE):
            raise TypeError("Argument toState must be of type components.State.")
        if not isinstance(event, LABELEDEVENT):
            raise TypeError("Argument event must be of type components.LabeledEvent.")

        arc = ARC(fromState, toState, event)

        return arc

class Automaton():

    # JAVA API: 

    def make(self, name, alphabet):

        aut = AUTOMATON(name)

        return aut


