import jpype

CLASSPATH = "/home/endre/Supremica/dist/Supremica.jar:/home/endre/Supremica/dist/SupremicaLib.jar:/home/endre/Supremica/dist/SupremicaTest.jar"
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % CLASSPATH)

STATE = jpype.JPackage("org").supremica.automata.State
LABELEDEVENT = jpype.JPackage("org").supremica.automata.LabeledEvent


class State:

    # TODO: Add API as comment
    # TODO: Add all args and isinstance them

    def make(self, name, initial = False, accepting = False, forbidden = False):

        args = [initial, accepting, forbidden]

        if not isinstance(name, str):
            raise TypeError("Argument name must be of type String.")
        for arg in args:
            if not isinstance(arg, bool):
                raise TypeError("Argument " + arg + " must be of type Boolean.")
        
        s = STATE(name)
    
        for arg in args:
            if arg == True:
                s.arg = True

        return s
    
    
class LabeledEvent:

    # API: clone, toString, getLabel, isControllable, setControllable, 
    #      isObservable, setObservable, isOperatorIncrease, setOperatorIncrease,
    #      isOperatorReset, setOperatorReset, isImmediate, setImmediate, 
    #      isPrioritized, setPrioritized, isUnobservable, setUnobservable,
    #      isProposition, setProposition, setExpansionPriority, 
    #      getExpansionPriority, equals, hashCode, getIndex, setIndex,
    #      compareTo, idForbidden, isTauEvent, getProxyInterface, refequals,
    #      refHashCode, acceptVisitor, getName, getKind, getAttributes

    def make(self, name, controllable = True,
                         prioritized = True,
                         observable = True,
                         tauEvent = False,
                         operatorIncrease = False,
                         operatorReset = False,
                         immediate = False,
                         proposition = False):

        args = [controllable,
                prioritized,
                observable,
                tauEvent,
                operatorIncrease, 
                operatorReset,
                immediate,
                proposition]

        if not isinstance(name, str):
            raise TypeError("Argument name must be of type String.")
        for arg in args:
            if not isinstance(arg, bool):
                raise TypeError("Argument " + arg + " must be of type Boolean.")
        
        e = LABELEDEVENT(name)
    
        for arg in args:
            if arg == True:
                e.arg = True

        return e

class Arc:

    # API: 
    def __init__(self):

        self.sup = jpype.JPackage("org").supremica.automata.Arc

    def make(self, name, event, fromState, toState, probability = 1):

        args = [event, fromState, toState, probability]

        # if not isinstance(name, str):
            # raise TypeError("Argument name must be of type String.")
        # if not isinstance(event, LABELEDEVENT):
            # raise TypeError("Argument event must be of type components.LabeledEvent.")
        # if not isinstance(fromState, State):
            # raise TypeError("Argument fromState must be of type components.State.")
        # if not isinstance(toState, State):
            # raise TypeError("Argument toState must be of type components.State.")
        # if not isinstance(probability, int):
            # raise TypeError("Argument probability must be of type Int.")

        arc = self.sup((fromState, toState, event))

        if probability != 1:
            arc.setProbability(probability)

        return arc
