import os

vaggelis_path = os.getenv("vaggelis")
panos_path = os.getenv("panos")

print("Vaggelis path is {}".format(vaggelis_path))
print("Panos path is {}".format(panos_path))

with open(vaggelis_path, 'r') as vag:
    print(vag.read())

with open(panos_path, 'r') as p:
    print(p.read())
