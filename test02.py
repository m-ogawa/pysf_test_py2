import sys
import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import pysoundfile as sf

plt.close("all")

filename = './test01_output.wav'
#filename = './sample.wav'
sig, fs = sf.read(filename)

sig_l = sig[:, 0]
sig_r = sig[:, 1]
n_fft = len(sig_l)

# FFT
Zs_l = fft.fft(sig_l, n_fft)
Zs_l = fft.fft(sig_l, n_fft)


# Plot
fig = plt.figure(1, figsize=(8, 8))
ax = fig.add_subplot(211)
ax.plot(sig_l[:1000])
ax.set_title("input signal")
ax.set_xlabel("time [pt]")
ax.set_ylabel("amplitude")

ax = fig.add_subplot(212)
ax.plot(Zs_l[0:fs/2])
ax.set_title("FFT result")
ax.set_xlabel("Freq [Hz]")
ax.set_ylabel("amplitude")

plt.show()