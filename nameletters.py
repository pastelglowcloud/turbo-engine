
txt= 'Alison Heck'
x = txt.split()
first= x[0].capitalize()
last= x[1].capitalize()
full= first + " " + last
    
def solve(s):
    x = s.split()
    full = x[0].capitalize() + " " + x[1].capitalize()
    return full

def solve(s):
    return s.split()[0].capitalize() + " " + s.split()[1].capitalize() 
