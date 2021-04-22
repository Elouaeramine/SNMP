import matplotlib.pyplot as plt
import csv
import time
import matplotlib.animation as animation 

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("debit.txt" ,"r").read()
    dataArray = pullData.split('\n')
    xar =[]
    yar=[]
    i=0
    for eachLine in dataArray :
        xar.append(i)
        i+=1
        yar.append(eachLine)

    ax1.clear()
    ax1.plot(xar,yar)


ani = animation.FuncAnimation(fig , animate , interval =1000)
plt.show()
