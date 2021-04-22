import matplotlib.pyplot as plt
import numpy as np
f=open("PBO100k.txt","r")
words=f.read()
newwords=words.replace(",",".")
newwords=newwords.replace(";"," ")
f2=open("PBO100k_2.txt","w")
f2.write(newwords)
f.close()
f2.close()
## Replace , to . ; to " ". This step is to better organize data
##In the mean time crate a second data file for the export

f3=open("PBO100k_2.txt","r")
s=f3.read().split()
data=list(float(i) for i in s[11:])

## put the data file from string into a list format; remove the top two useless line and store them in data as float

for i in range(len(data)):
	if i%6==1:
		del data[0]
	else:
		data.append(data[0])
		del data[0]
		
## remove the temperature line which is useless
time=[]
force=[]
distance=[]
stress=[]
strain=[]
lamda=[]
for i in range(0,len(data),5):
	time.append(data[i])
	force.append(data[i+1])
	distance.append(data[i+2])
	stress.append(data[i+3])
	strain.append(data[i+4])
for i in range(len(time)):
	lamda.append(strain[i]+1)

plt.plot(distance,force)
plt.xlabel('Gap distance(mm)')
plt.ylabel('Force(N)')
plt.grid(linestyle='--')
plt.savefig('Distance_force.pdf')
f3.close()
