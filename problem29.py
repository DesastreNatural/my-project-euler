r=set([])
for a in xrange(2,101):
  for b in xrange(2,101):
    r.add(a**b)
print len(r)