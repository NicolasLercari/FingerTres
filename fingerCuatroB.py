import sys
n=int(sys.argv[1])
i=2
j=1
while i<n:
	if n%i==0:j=0;i=n
	i+=1
print j
