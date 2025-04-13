import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import math

N = 3 * 1024
f = np.linspace(0, 512, int(N / 2))

t = np.linspace(0, 3, 12 * 1024)
x = np.zeros_like(t)
Fi = [130.81, 146.83, 164.81, 174.61, 196, 220, 246.93]
fi = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88]
ti = 0
Ti = 0


def unit(y):
    return np.where(y < 0, 0, 1)

n = 1
while n <= 5:
    Ti = 0.5
    x += ((np.sin(2 * np.pi * Fi[n] * t) + np.sin(2 * np.pi * fi[n] * t)) * (unit(t - ti) - unit(t - ti - Ti)))
    ti += 0.7
    n += 1


#sd.play(x, 3 * 1024)



f = np.linspace(0 , 512 , (int)(N/2))

#x in frequency domain
x_f = fft(x)
x_f = 2/N * np.abs(x_f [0:int(N/2)])
plt.figure()
plt.subplot(2,1,1)
plt.stem(t,x)
plt.subplot(2,1,2)
plt.stem(f,x_f)


fn1,fn2 =  np.random.randint(0, 512,2)
print(fn1)
print(fn2)


#noise generated for time domain
n_t = np.sin(2*fn1*np.pi*t)+np.sin(2*fn2*np.pi*t)

#x in time domain after adding noise
xn = x + n_t


#sd.play(xn,3*1024)




#x in frequency domain after adding noise
xn_f = fft(xn)
xn_f = 2/N * np.abs(xn_f [0:(int)(N/2)])
plt.figure()
plt.subplot(2,1,1)
plt.stem(t,xn)
plt.subplot(2,1,2)
plt.stem(f,xn_f)

#array containing the two frequencies with the very high peaks
f_array = f[xn_f > np.max(x_f) + 0.5]

f1 = int (f_array[0])
f2 = int(f_array[1])

x_filtered = xn - (np.sin(2*f1*np.pi*t)+np.sin(2*f2*np.pi*t))

x_f_filtered = fft(x_filtered)
x_f_filtered = 2/N * np.abs(x_f_filtered [0:int(N/2)])
plt.figure()
plt.subplot(2,1,1)
plt.stem(t,x_filtered)
plt.subplot(2,1,2)
plt.stem(f,x_f_filtered)


sd.play(x_filtered, 3* 1024)
