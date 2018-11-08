import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
plt.clf()

duration = 10.
dt = 0.1
N = int(duration/dt)

#Process noise
noise1 = 9797185771745235
noise2 = 2485205224588954
noise3 = 3053123663654248

#Process sigma
sigma1 = 235281220233811 
sigma2 = 248180438667464
sigma3 = 457589124776989
