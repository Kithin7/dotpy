import random as rng
import numpy as np
import matplotlib.pyplot as plt


X = 100000 #6 for character stats, or large X for study

##initialize
Set = np.zeros((0),dtype=int)
Sums = np.zeros((0),dtype=int)
Ind=0
print("Rolling some dice...")
## roll 4d6 X times
for I in range(0,X):
    for J in range(0,4):
        Set = np.append(Set,[[rng.randint(1,6)]])
    SUM = (Set[Ind] +Set[Ind+1] +Set[Ind+2] +Set[Ind+3])-min(Set[Ind],Set[Ind+1],Set[Ind+2],Set[Ind+3])
    Sums = np.append(Sums, SUM)
    Ind = Ind+4
    if I == round(.01*X):
        print('... 1%')
    elif I == round(.1*X):
        print('...10%')
    elif I == round(.25*X):
        print('...25%')
    elif I == round(.5*X):
        print('...50%')
    elif I == round(.75 * X):
        print('...75%')
    elif I == round(.87*X):
        print('...almost there...')
#print("Set = ",Set)
#print("Sums = ",Sums)
print("Done rolling!")

##plotting
x=np.array(range(3,19,1))
y=np.array([],dtype=int)
NUM=3
for L in range(3,19,1):
    y = np.append(y,(Sums==NUM).sum())
    NUM=NUM+1
#print("x=",x)
#print("y=",y)
yP = y /np.sum(y) *100

print("Preparing graphs...")
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.bar(x,yP,edgecolor="white",linewidth=1)
ax.set(xlim=(2.5,18.5),xticks=np.arange(3,19),
       ylim=(0,np.ceil(np.amax(yP))),yticks=np.arange(0,np.ceil(np.amax(yP)),np.ceil(np.amax(yP)/10)))
ax.set_xlabel('sum of 4d6-low')
ax.set_ylabel('% occurance')
TITLE = 'n = ' + str(X)
ax.set_title(TITLE)
print("Complete!\nWaiting for user...")
plt.tight_layout()
plt.show()
