#print sum([(x**2)*((-1)**x)*(-1) for x in range(1,11)])
print sum([x**2 if x%2 == 1 else -x**2 for x in range(1,11)])
