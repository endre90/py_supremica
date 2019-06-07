from components.state import State
#print(State)
s = State()
s1 = s.make('s1')

print(s1)
print(s1.isInitial())
s1.setInitial(True)

print(s1.isInitial())

s1.setInitial(False)
print(s1.isInitial())
