from itertools import permutations

x = 1
y = 1
z = 2
n = 2
    
num_list = [x,y,z]
digits = [str(digit) for digit in  num_list]
num_permutations = permutations(num_list,3)
print(digits)
print(num_permutations)

# a = permutations([x,y,z],3) 
# for i in a: 
#     if sum(i)!=n:
#         print(list(i)) 

# print([i for i in a if sum(i)!=n])

print([i for i in list(permutations([x,y,z],3)) if sum(i)!=n])

# print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if sum[a,b,c]!=n])