import jpype
import ast

# start the JVM with the good classpaths
classpath = "/home/endre/Supremica/dist/Supremica.jar:/home/endre/Supremica/dist/SupremicaLib.jar" # :lib/nekohtml-1.9.13.jar:lib/xerces-2.9.1.jar"
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % classpath)

# get the Java classes we want to use
Event = jpype.JPackage("org").supremica.automata.LabeledEvent
State = jpype.JPackage("org").supremica.automata.State
StateSet = jpype.JPackage("org").supremica.automata.StateSet
Alphabet = jpype.JPackage("org").supremica.automata.Alphabet
Arc = jpype.JPackage("org").supremica.automata.Arc
Automaton = jpype.JPackage("org").supremica.automata.Automaton

EVENTS = ['1', '2', '3']
STATES = ['1', '2', '3']

e = {}
for ev in EVENTS:
    e['{}'.format(ev)] = Event('e_' + ev)

s = {}
for st in STATES:
    s['{}'.format(st)] = State('s_' + st)

s['1'].setInitial(False)
s['2'].initial = False

print(State.isInitial(s['1']))
print(State.isInitial(s['2']))
print(State.isInitial(s['3']))

TRANS = [(s['1'], s['2'], e['1']),
         (s['2'], s['3'], e['2'])]

t = {}
for tr in TRANS:
    t['{}'.format(TRANS.index(tr))] = Arc(TRANS[TRANS.index(tr)][0], 
                                          TRANS[TRANS.index(tr)][1], 
                                          TRANS[TRANS.index(tr)][2])

a = Automaton("1")


print(t['0'])
print(t['1'])