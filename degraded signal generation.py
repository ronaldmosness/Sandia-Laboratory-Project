# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:53:23 2024

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

noise_amplitude = 0.9  # Adjust the noise amplitude as needed
gaussian_noise = np.random.normal(0, noise_amplitude, len(eeg_signal1))
eeg_with_noise1 = eeg_signal1 + gaussian_noise
eeg_with_noise2 = eeg_signal2 + gaussian_noise
eeg_with_noise3 = eeg_signal3 + gaussian_noise
eeg_with_noise4 = eeg_signal4 + gaussian_noise
eeg_with_noise5 = eeg_signal5 + gaussian_noise
noise_amplitude1 = 0.5  # Adjust the noise amplitude as needed
gaussian_noise1 = np.random.normal(0, noise_amplitude1, len(eeg_signal1))
eeg_with_noise6 = eeg_signal6 + gaussian_noise1
eeg_with_noise7 = eeg_signal7 + gaussian_noise1
eeg_with_noise8 = eeg_signal8 + gaussian_noise1
eeg_with_noise9 = eeg_signal9 + gaussian_noise1
eeg_with_noise10 = eeg_signal10 + gaussian_noise

np.savetxt('eegd9.csv', eeg_with_noise1, delimiter=',')
np.savetxt('eegd10.csv', eeg_with_noise2, delimiter=',')
np.savetxt('eegd11.csv', eeg_with_noise3, delimiter=',')
np.savetxt('eegd12.csv', eeg_with_noise4, delimiter=',')
np.savetxt('eegd13.csv', eeg_with_noise5, delimiter=',')
np.savetxt('eegd14.csv', eeg_with_noise6, delimiter=',')
np.savetxt('eegd15.csv', eeg_with_noise7, delimiter=',')
np.savetxt('eegd16.csv', eeg_with_noise8, delimiter=',')
np.savetxt('eegd17.csv', eeg_with_noise9, delimiter=',')
np.savetxt('eegd18.csv', eeg_with_noise10, delimiter=',')