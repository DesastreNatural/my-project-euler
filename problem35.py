import psyco
psyco.full()
def eras(n):
  siv=range(n+1)
  siv[1]=0
  sqn=int(round(n**0.5))
  for i in range(2,sqn+1):
    if siv[i]!=0:
        siv[2*i:n/i*i+1:i]=[0]*(n/i-1)
  return filter(None,siv)

def circular1(x):
  s=str(x)
  new=""
  for i in xrange(1,len(s)+1):
    new=new+(s[i%(len(s))])
  return new
def circular(x):
  res=[str(x)]
  for i in xrange(len(str(x))-1):
    res.append(circular1(res[i]))
  return map(int,res)
def is_circular_prime(x,primes):
  for j in circular(primes[i]):
    if not(j in primes):
      return False
s=set([])
lim=100
print "Generating Primes..."
primes=eras(lim)
print len(primes)
i=0
while(i<len(primes)):
  if is_circular_prime(primes[i],primes):
    for j in circular(primes[i]):
      s.add(j)
  i=i+1
print s
print len(s)