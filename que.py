string = input(":")
k = int(input(":"))

for i in range(0, len(string), k):
    t = []
    seen = set()
    
    for j in string[i:i+k]:
        if j not in seen:
            seen.add(j)
            t.append(j)
    
    print("".join(t))

string = input(":")
k = int(input(":"))

for i in range(0, len(string), k):
    print("".join(dict.fromkeys(string[i:i+k])))