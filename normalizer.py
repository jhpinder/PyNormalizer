#! python

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
import soundfile as sf

Tk().withdraw()
filename = askopenfilename()
data, fs = sf.read(filename)
maxL = max(np.abs(data[:,0]))
maxR = max(np.abs(data[:,1]))
maxVal = max(maxL, maxR)
data = data / maxVal

sf.write(filename.split('.')[0] + "_normalized.wav", data, fs)
print(filename)
