#! python

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
import wavio as w
import PyWave as pw

Tk().withdraw()
filename = askopenfilename()
#wf = w.read(filename)
wf = pw.open(filename)
data = wf.read()
fs = wf.frequency
print(data)
maxL = max(np.abs(data[:,0]))
maxR = max(np.abs(data[:,1]))
maxVal = max(maxL, maxR)
data = data / maxVal

w.write(filename.split('.')[0] + "_normalized.wav", data, fs, sampwidth=3)
print(filename)
