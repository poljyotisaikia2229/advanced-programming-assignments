# assignment_14.py
import sys
import gc


class Node:
    def __init__(self, name):
        self.name = name
        self.link = None

    def __repr__(self):
        return f"Node({self.name!r})"


# Stop automatic garbage collection so the cycle stays in memory
gc.disable()

# Create nodes
A = Node("A")
B = Node("B")

# Create cycle
A.link = B # type: ignore
B.link = A # type: ignore

# Save object IDs so we can look for them after del
a_id = id(A)
b_id = id(B)

print("Before deletion:")
print("A:", A)
print("B:", B)
print("sys.getrefcount(A):", sys.getrefcount(A))
print("sys.getrefcount(B):", sys.getrefcount(B))

# Delete normal references
del A
del B

print("\nAfter del A and del B:")

# Investigate unreachable cycle still in memory
found = [
    obj for obj in gc.get_objects()
    if id(obj) in (a_id, b_id)
]

print("Objects still found in memory:")
for obj in found:
    print(obj, "links to", obj.link)

# Force garbage collection
collected = gc.collect()

print("\nAfter gc.collect():")
print("Unreachable objects collected:", collected)

# Confirm cleanup
found_after = [
    obj for obj in gc.get_objects()
    if id(obj) in (a_id, b_id)
]

print("Objects found after collection:", found_after)

gc.enable()