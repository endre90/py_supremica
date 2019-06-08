from components import State
from components import LabeledEvent
from components import Arc
from components import Alphabet
from components import Automaton
from generator import Generator


states = ['s1', 's2', 's3', 's4', 's5']
events = ['e1', 'e2', '!e3', '!e4', 'e5']
trans = [('s1', 's2', 'e1'), ('s2', 's3', '!e3')]

g = Generator()
aut1 = g.generate_automaton('aut1', events, states, trans)

print(aut1.nbrOfTransitions())
print(aut1.getTransitions())
print(aut1)

'''

# for s in states:

# for s in states:
#     a = lambda: exec('global x; x = 1')
#     exec("s = 's'")
#g = Generator()
#st = g.generate_states(states)


#print(State)
s = State()
e = LabeledEvent()
s1 = s.make('s1')
s2 = s.make('s2')
s3 = s.make('s3')
e1 = e.make('e1')
e2 = e.make('e2')
e3 = e.make('e3')

print("===========")
print(e2.isControllable())
print(e2.setControllable(False))
print(e2.isControllable())
print("===========")

print(s1)
print(e1)
print(s1.isInitial())
s1.setInitial(True)
print("===========")
print(e1.getKind())
# 
# 
print(s1.isInitial())
# 
s1.setInitial(False)
print(s1.isInitial())

a = Arc()
a1 = a.make('t1', s1, s2, e1)
a2 = a.make('t2', s2, s3, e2)
print(a1)
print(a2)

alph = Alphabet()
alph1 = alph.make()
alph1.addEvent(e1)
alph1.addEvent(e2)


aut = Automaton()
aut1 = aut.make('aut1', alph1)
aut1.addState(s1)
aut1.addState(s2)
aut1.addState(s3)

#alph1 = [e1, e2, e3]

aut1.addArc(a1)
aut1.addArc(a2)

print(alph1)
print(aut1.nbrOfTransitions())
print(aut1.getTransitions())
print(aut1)
'''