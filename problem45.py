import psyco
psyco.full()

def triangular(n):
  return (((n*n)+n)/2)
def pentagonal(n):
  return (((n*n*3)-n)/2)
def hexagonal(n):
  return ((2*n*n)-n)

tn=[triangular(i) for i in xrange(10000,100000)]
pn=[pentagonal(i) for i in xrange(10000,100000)]
hn=[hexagonal(i) for i in xrange(10000,100000)]
for i in tn:
  if (i in pn) and (i in hn):
    print i

