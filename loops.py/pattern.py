row = 7
for i in range(row):
    print( " "*(row-i) + "*" * (2*i-1))
for i in range(row-1,0,-1):
    print( " "*(row-i) + "*" * (2*i-1))