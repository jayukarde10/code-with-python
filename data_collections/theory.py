# 📘 Python List – Important Methods (Quick Revision)

l = [10, 20, 30]

# 🟢 Add Elements
l.append(40)              # Add single element at end
l.extend([50, 60])        # Add multiple elements
l.insert(1, 15)           # Insert at specific index

# 🔴 Remove Elements
l.remove(20)              # Remove specific value (first occurrence)
l.pop()                   # Remove last element
l.pop(0)                  # Remove element at index
l.clear()                 # Remove all elements

# 🔵 Access Elements
print(l[0])               # Access by index
print(l[-1])              # Last element
print(l[1:3])             # Slicing

# 🟣 Update Elements
l[0] = 100                # Update value at index

# 🟡 View / Info
len(l)                    # Length of list
l.count(30)               # Count occurrences
l.index(30)               # Get index of value

# 🟤 Sorting & Reversing
l.sort()                  # Sort ascending
l.sort(reverse=True)      # Sort descending
l.reverse()               # Reverse list order

# ⚪ Looping
for item in l:
    print(item)

# 🟠 Copy List
new_l = l.copy()          # Copy list


# 📘 Python Tuple – Important Methods (Quick Revision)

t = (10, 20, 30, 20)

# 🔵 Access Elements
print(t[0])        # First element
print(t[-1])       # Last element
print(t[1:3])      # Slicing

# 🟢 Tuple Methods (Only 2 main methods)

t.count(20)        # Count occurrences of a value
t.index(30)        # Get index of a value

# 🟡 Looping
for item in t:
    print(item)

# 🟣 Tuple Length
len(t)             # Get length

# 🟤 Convert Tuple ↔ List (because tuple is immutable)

l = list(t)        # Convert to list (to modify)
l.append(40)
t = tuple(l)       # Convert back to tuple

# ⚪ Tuple Packing & Unpacking
a, b, c, d = t     # Unpacking
print(a, b)

# 🟠 Single Element Tuple
single = (10,)     # Comma is compulsory


# 📘 Python Set – Important Methods (Quick Revision)

s = {10, 20, 30}

# 🟢 Add Elements
s.add(40)                  # Add single element
s.update([50, 60])         # Add multiple elements

# 🔴 Remove Elements
s.remove(20)               # Remove element (error if not found)
s.discard(100)             # Remove element (NO error if not found)
s.pop()                    # Remove random element
s.clear()                  # Remove all elements

# 🔵 Set Operations (Very Important)

a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)                 # Union → {1,2,3,4,5}
a.intersection(b)          # Intersection → {3}
a.difference(b)            # Difference → {1,2}
a.symmetric_difference(b)  # Symmetric Difference → {1,2,4,5}

# 🟣 Operators Version (Shortcut)

a | b      # Union
a & b      # Intersection
a - b      # Difference
a ^ b      # Symmetric Difference

# 🟡 Check Methods
3 in a                     # Membership check
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)

# 🟤 Looping
for item in s:
    print(item)

# ⚪ Length
len(s)


# 📘 Python Dictionary – Important Methods (Quick Revision)

d = {"name": "Jay"}

# 🟢 Add / Update
d["age"] = 20                      # Add or update single key
d.update({"city": "Mumbai"})       # Add or update using update()
d.update({"age": 21, "college": "APSIT"})  # Update multiple keys

# 🔴 Remove
del d["age"]        # Delete specific key (error if not found)
d.pop("city")       # Remove & return value
d.popitem()         # Remove last inserted item
d.clear()           # Remove all items

# 🔵 Access
print(d["name"])                 # Normal access (error if not found)
print(d.get("salary"))           # Safe access (returns None)
print(d.get("salary", "NA"))     # Safe with default value

# 🟣 View
d.keys()      # All keys
d.values()    # All values
d.items()     # Key-value pairs

for key, value in d.items():     # Loop dictionary
    print(key, value)

# 🟡 Copy
new_d = d.copy()                 # Copy dictionary



