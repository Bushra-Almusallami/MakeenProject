#Create a list of 100 random pair of integers (x,y) between 1 and 100. Draw visualization
#of the data using different

import matplotlib.pyplot as plt
import numpy as np

data= np.random.randint(1,101, size=(10,2))
print("Origenal numbers:\n",data)

#create a figure with subplots to plot different scatter plot style
figure, axs= plt.subplots(2,2, figsize=(10,10))

#plot the data using different scatter plot
axs[0, 0].scatter(data[:, 0], data[:, 1], c='red')
axs[0, 0].set_title('Default')
axs[0, 1].scatter(data[:, 0], data[:, 1], c='blue', marker='x')
axs[0, 0].set_title('Cross')
axs[1,0].scatter(data[:, 0], data[:, 1], c='green', marker='s')
axs[1, 0].set_title('Square')
axs[1,1].scatter(data[:, 0], data[:, 1], c='purple', marker='^')
axs[1, 1].set_title('Triangle Up')

#set the title of the figure
figure.suptitle('ScatterPlots of Random Pairs of Integers')

#show the plot
plt.show()
