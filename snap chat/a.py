def power(x, y):
    if y == 0:
        return 1
    else:
        print(x)
        print(y)
        return x * power(x, y-1)
        
		
print(power(2, 3))