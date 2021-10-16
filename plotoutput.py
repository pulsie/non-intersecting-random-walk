#histogram from https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py
import matplotlib.pyplot as plt
import numpy as np
with open("output.txt") as f:
    outputstrings = f.readlines()
stepVector=[]
for i in outputstrings:
    stepVector.append(int(i))
#histo from https://pythonspot.com/matplotlib-histogram/
num_bins = 100
n, bins, patches = plt.hist(stepVector, num_bins, facecolor='blue', alpha=0.5)
plt.show()
