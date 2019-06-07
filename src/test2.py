from components import State
from components import LabeledEvent
from components import Arc
#print(State)
s = State()
e = LabeledEvent()
s1 = s.make('s1')
s2 = s.make('s2')
e1 = e.make('e1')

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
print(a1)


