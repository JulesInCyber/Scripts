'''
This tool was created for the Blue Team Labs Online Challenge "Spectrum".
It can be used to visualize any given .wav file
'''

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import spectrogram
from termcolor import colored
import os
 
file_name = input(colored("[?] Please Specify File Path: ", "cyan"))
save_as = file_name.split(".")[0]

rate, data = wav.read(file_name)
if data.ndim > 1:
    data = data[:, 0]

frequencies, times, Sxx = spectrogram(data, fs=rate, nperseg=256)
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx + 1e-10), shading='gouraud', cmap='inferno')
# plt.ylim(0, 12000)
plt.title(f"Spectogram of {save_as}")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.colorbar(label="Intensity [dB]")

confirm_save = input("[?] Do you want to save the file? (y/n)")

if confirm_save == "y":
    work_dir = os.getcwd()
    plt.savefig(f"{save_as}.png", dpi=300)
    print(colored(f"[!] Saved as {work_dir}/{save_as}.png", "yellow"))

plt.show()
