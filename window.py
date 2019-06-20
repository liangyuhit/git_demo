# -*- coding: utf-8 -*-
'''
Created on 19.06.2019

@author: yu03
'''

from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
import numpy as np

window_boxcar = signal.boxcar(51)
A_boxcar = fft(window_boxcar, 2048) / (len(window_boxcar)/2.0)
freq_boxcar = np.linspace(-0.5, 0.5, len(A_boxcar))
response_boxcar = 20 * np.log10(np.abs(fftshift(A_boxcar / abs(A_boxcar).max())))

window_hanning = signal.windows.hann(51)
A_hanning = fft(window_hanning, 2048) / (len(window_hanning)/2.0)
freq_hanning = np.linspace(-0.5, 0.5, len(A_hanning))
response_hanning = np.abs(fftshift(A_hanning / abs(A_hanning).max()))
response_hanning = 20 * np.log10(np.maximum(response_hanning, 1e-10))

window_hamming = signal.hamming(51)
A_hamming = fft(window_hamming, 2048) / (len(window_hamming)/2.0)
freq_hamming = np.linspace(-0.5, 0.5, len(A_hamming))
response_hamming = 20 * np.log10(np.abs(fftshift(A_hamming / abs(A_hamming).max())))

window_blackman = signal.windows.blackman(51)
A_blackman = fft(window_blackman, 2048) / (len(window_blackman)/2.0)
freq_blackman = np.linspace(-0.5, 0.5, len(A_blackman))
response_blackman = np.abs(fftshift(A_blackman / abs(A_blackman).max()))
response_blackman = 20 * np.log10(np.maximum(response_blackman, 1e-10))

window_gaussian = signal.gaussian(51, std=7)
A_gaussian = fft(window_gaussian, 2048) / (len(window_gaussian)/2.0)
freq_gaussian = np.linspace(-0.5, 0.5, len(A_gaussian))
response_gaussian = 20 * np.log10(np.abs(fftshift(A_gaussian / abs(A_gaussian).max())))

plt.figure('window response')

plt.subplot(5,2,1)
plt.plot(window_boxcar)
plt.title("Boxcar window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.subplot(5,2,2)
plt.plot(freq_boxcar, response_boxcar)
plt.axis([-0.5, 0.5, -120, 0])
plt.title("Frequency response of the Boxcar window")
plt.ylabel("Normalized magnitude [dB]")

plt.subplot(5,2,3)
plt.plot(window_hanning)
plt.title("Hanning window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.subplot(5,2,4)
plt.plot(freq_hanning, response_hanning)
plt.axis([-0.5, 0.5, -120, 0])
plt.title("Frequency response of the Hann window")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")


plt.subplot(5,2,5)
plt.plot(window_hamming)
plt.title("Hamming window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.subplot(5,2,6)
plt.plot(freq_hamming, response_hamming)
plt.axis([-0.5, 0.5, -120, 0])
plt.title("Frequency response of the Hamming window")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")

plt.subplot(5,2,7)
plt.plot(window_blackman)
plt.title("Blackman window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.subplot(5,2,8)
plt.plot(freq_blackman, response_blackman)
plt.axis([-0.5, 0.5, -120, 0])
plt.title("Frequency response of the Blackman window")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")


plt.subplot(5,2,9)
plt.plot(window_gaussian)
plt.title("Gaussian window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.subplot(5,2,10)
plt.plot(freq_gaussian, response_gaussian)
plt.axis([-0.5, 0.5, -120, 0])
plt.title(r"Frequency response of the Gaussian window ($\sigma$=7)")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")

plt.get_current_fig_manager().window.setGeometry(20, 50, 1000, 1800)
plt.show()