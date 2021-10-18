#histogram from https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py
import matplotlib.pyplot as plt
import numpy as np
with open("output.txt") as f:
    outputstrings = f.readlines()
with open("output_smartalgo.txt") as f2:
    outputstrings2 = f2.readlines()
stepVector1=[]
stepVector2=[]
for i in outputstrings:
    stepVector1.append(int(i))
for i in outputstrings2:
    stepVector2.append(int(i))
bins = range(0,400,5)
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
axs[0].hist(stepVector1, bins=bins)
axs[1].hist(stepVector2, bins=bins)
plt.show()

