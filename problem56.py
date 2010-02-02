def digitsum(s):
  res=0
  for i in str(s):
    res=res+int(i)
  return res

res=[]
for i in xrange(101):
  for j in xrange(101):
    res.append(digitsum(i**j))
print max(res)