from itertools import permutations
password = ['a', 'b']
password_1 = ['a', 'b', 'c']
password_2 = ['a', 'b', 'c', 'd']
password_3 = ['a', 'b', 'c', 'd', 'e']

# print(list(permutations(password)))
x = list(permutations(password))
x_1 = list(permutations(password_1))
x_2 = list(permutations(password_2))
x_3 = list(permutations(password_3))
print("\n" + "\n" + "\n")
print(len(x))

print("\n")
print(len(x_1)) 

print("\n")
print(len(x_2)) 

print("\n")
print(len(x_3)) 