d = {'a': 1, 'l': 2, 'e': 3}
new_d = {'n': 4, 'a': 5}
d.update(new_d)
print(d)

d2 = {'a': 1, 'l': 2, 'e': 3}
del d2['a']
print (d2)

d3 = {'a': 1, 'l': 2, 'e': 3}
d3.clear()
print(d3)

d4 = {'a': 1, 'l': 2, 'e': 3}
k = d4.keys()
print(k)

d5 = {'a': 1, 'l': 2, 'e': 3}
v = d5.values()
print(v)

d5 = {'a': 1, 'l': 2, 'e': 3}
i = d5.items()
print(i)
