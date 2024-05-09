# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:00:59 2024

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_dummy_eeg(duration=10, sampling_rate=1000, noise_level=0.5):
    time_points = np.arange(0, duration, 1/sampling_rate)
    
    # Generate random noise
    noise = np.random.normal(0, noise_level, len(time_points))
    
    # Create a sine wave resembling brainwave patterns
    theta = 8  # Frequency in Hz
    sine_wave = np.sin(2 * np.pi * theta * time_points)
    
    # Combine noise and sine wave to simulate EEG signal
    eeg_signal = noise + sine_wave
    
    return time_points, eeg_signal

# Example usage
duration = 10  # seconds
sampling_rate = 1000  # Hz
noise_level = 0.5

time_points1, eeg_signal1 = generate_dummy_eeg(duration, sampling_rate, noise_level)
time_points1, eeg_signal2 = generate_dummy_eeg(duration, sampling_rate, noise_level)
time_points1, eeg_signal3 = generate_dummy_eeg(duration, sampling_rate, noise_level)
time_points1, eeg_signal4 = generate_dummy_eeg(duration, sampling_rate, noise_level)
time_points1, eeg_signal5 = generate_dummy_eeg(duration, sampling_rate, noise_level)
time_points1, eeg_signal6 = generate_dummy_eeg(duration, sampling_rate, noise_level)
time_points1, eeg_signal7 = generate_dummy_eeg(duration, sampling_rate, noise_level)
time_points1, eeg_signal8 = generate_dummy_eeg(duration, sampling_rate, noise_level)
time_points1, eeg_signal9 = generate_dummy_eeg(duration, sampling_rate, noise_level)
time_points1, eeg_signal10 = generate_dummy_eeg(duration, sampling_rate, noise_level)

np.savetxt('eegh9.csv', eeg_signal1, delimiter=',')
np.savetxt('eegh10.csv', eeg_signal2, delimiter=',')
np.savetxt('eegh11.csv', eeg_signal3, delimiter=',')
np.savetxt('eegh12.csv', eeg_signal4, delimiter=',')
np.savetxt('eegh13.csv', eeg_signal5, delimiter=',')
np.savetxt('eegh14.csv', eeg_signal6, delimiter=',')
np.savetxt('eegh15.csv', eeg_signal7, delimiter=',')
np.savetxt('eegh16.csv', eeg_signal8, delimiter=',')
np.savetxt('eegh17.csv', eeg_signal9, delimiter=',')
np.savetxt('eegh18.csv', eeg_signal10, delimiter=',')





# Plot the generated EEG signal
'''plt.plot(time_points, eeg_signal)
plt.title('Dummy EEG Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.show()'''
