from automata_generator import Generator
from automata_synchronizer import Synchronizer

states1 = ['s1', 's2', 's3']
states2 = ['s1', 's2', 's3']
alphabet1 = ['a', 'b']
alphabet2 = ['a', 'c']
u_alphabet = []
arcs1 = [('t1', 's1', 's2', 'a'), ('t2', 's2', 's3', 'b')]
arcs2 = [('t1', 's1', 's2', 'a'), ('t4', 's2', 's3', 'c')]
init1 = 's1'
init2 = 's2'
marked1 = ['s3']
marked2 = ['s3']
forbidden1 = []
forbidden2 = []

g = Generator()
aut1 = g.generate_automaton('aut1', states1, alphabet1, u_alphabet, arcs1, init1, marked1, forbidden1)
aut2 = g.generate_automaton('aut2', states2, alphabet2, u_alphabet, arcs2, init2, marked2, forbidden2)

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

s = Synchronizer()
auts = s.synchronize_automata([aut1, aut2])
print(auts.getNumberOfStates())