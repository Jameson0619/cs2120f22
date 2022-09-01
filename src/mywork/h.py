from z3 import *
from itertools import combinations

def at_most_one(literals):
    c = []
    for pair in combinations(literals, 2):
        a, b = pair[0], pair[1]
        c += [Or(Not(a), Not(b))]
    return And(c)


#Create all the literals
x = [[Bool("x_%i_%i" % (i,j)) for j in range(5) for i in range(5)]]

#Create a solver instance
s = Solver()

#Add all the constraints
#At least 5 queens
for i in range(5):
    s.add(Or(x[i])) #at least one queen per row
    
#Constraints: at most one queen per row
#at most one queen per column
for i in range(5):
    col = []
    for j in range(5):
        col += [x[j][i]]
    s.add(at_most_one(col))
    s.add(at_most_one(x[i]))
    
print(s.check)

