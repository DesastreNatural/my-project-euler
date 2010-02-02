def fac(n):
  if n==0:
    return 1
  else:
    return n*fac(n-1)
lim=1000000
counter=0
s=map(fac,range(101))
for n in xrange(101):
  for r in xrange(n+1):
    if (s[n]/((s[r])*(s[n-r])))>lim:
      counter=counter+1
print counter
    