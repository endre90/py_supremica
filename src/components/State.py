import jpype

# Set valid class path for Supremica archives
CLASSPATH = "/home/endre/Supremica/dist/Supremica.jar:/home/endre/Supremica/dist/SupremicaLib.jar:/home/endre/Supremica/dist/SupremicaTest.jar"

class State:

    def __init__(self):

        jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % CLASSPATH)
        self.sup_state = jpype.JPackage("org").supremica.automata.State

    def make(self, name, initial = False, accepting = False, forbidden = False):

        args = [initial, accepting, forbidden]

        if not isinstance(name, str):
            raise TypeError("Argument name must be String.")
        for arg in args:
            if not isinstance(arg, bool):
                raise TypeError("Argument " + arg + " must be Boolean.")
        
        s = self.sup_state(name)
    
        for arg in args:
            if arg == True:
                s.arg = True

        return s