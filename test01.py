import numpy as np
#import matplotlib.pyplot as plt
import pysoundfile as sf

time = 2.0
fs = 44100
freq = 880.0

t = np.linspace(start=0, stop=(2*np.pi)*time*freq, num=time*fs-1, endpoint=False)
sig = np.sin(t)
sig2 = np.array([sig, sig]).T

#sf.write(file='./test01_output.wav', data=sig, samplerate=fs, exclusive_creation=False)
sf.write(file='./test01_output.wav', data=sig2, samplerate=fs, exclusive_creation=False)

print(sig2)
print(sig2.shape[1])
