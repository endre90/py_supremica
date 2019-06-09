from generator import Generator

states = ['s1', 's2', 's3', 's4', 's5', 's6']
alphabet = ['e1', 'e2', 'e3', 'e4', 'e5']
u_alphabet = ['e3', 'e4']
arcs = [('t1', 's1', 's2', 'e1'), ('t2', 's2', 's3', 'e3')]
init = 's1'
marked = ['s4', 's5']
forbidden = ['s2', 's6']

g = Generator()
aut1 = g.generate_automaton('aut1', states, alphabet, u_alphabet, arcs, init, marked, forbidden)

# Some tryouts
print(aut1.getStates())
print(aut1.getAlphabet())
print(aut1.getTransitions())
print(aut1.getAlphabet().getUncontrollableAlphabet())
print(aut1.getAlphabet().getControllableAlphabet())

for s in aut1.getStates():
    if s.isAccepting():
        print("marked")
        print(s)
    if s.isInitial():
        print("initial")
        print(s)
    if s.isForbidden():
        print("forbidden")
        print(s)