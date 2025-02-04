import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq

# fft: If the input signal is complex, output positive and negative frequencies
# rff: If the signal is real-valued, output positive frequencies

# Data for forces
force_data = np.loadtxt('postProcessing/FO_forces/0/force.dat')
time = force_data[:, 0]
Fx = force_data[:, 1]
Fy = force_data[:, 2]

# Data for force coefficients
coeff_data = np.loadtxt('postProcessing/forceCoeffs/0/coefficient.dat')
coeff_time = coeff_data[:, 0]
Cd = coeff_data[:, 1]
Cl = coeff_data[:, 4]

L = 2  # Characteristic length (diameter)
U = 1  # Flow velocity

index = np.where(coeff_time >= 180)[0][0] # Index when the time > 120 s

n_samples = len(Cl[index:]) # Number of samples
# normalize = n_samples/2
SAMPLE_RATE = 1 / (time[2] - time[1]) # Sample rate Hz

cl_fft = rfft(Cl[index:]) # FTT of the lift coefficient
frequency = rfftfreq(n_samples, 1 / SAMPLE_RATE) # Frequencies of the FFT
shed_freq = frequency[np.argmax(np.abs(cl_fft))] # Maxium frequency from 
# print(n_samples)

print('D = {:.6f}'.format( np.average(Fx[index:])) )
print('L = {:.6f}'.format( np.average(Fy[index:])) )

print('Cd = {:.6f}'.format( np.average(Cd[index:])) )
print('Cl (avg) = {:.6f}'.format( np.average(Cl[index:])) )
print('Cl (amplitude) = {:.6f}'.format( np.max(2*np.abs(cl_fft)/n_samples)) )
print('Frequency = {:.6f} Hz'.format(shed_freq) )
print('Strouhal  = {:.6f}'.format( shed_freq * L / U ))

# Plotting Forces
plt.figure(1, figsize=(8, 6))
plt.plot(time, Fx, c='r', label='Fx')
plt.plot(time, Fy, c='b', label='Fy')
plt.xlabel('Time')
plt.ylabel('Force')
plt.title('Forces')
plt.legend()
# plt.show()

# Plotting Force Coefficients
plt.figure(2, figsize=(8, 6))
plt.plot(coeff_time, Cd, c='r', label='Cd')
plt.plot(coeff_time, Cl, c='b', label='Cl')
plt.xlabel('Time')
plt.ylabel('Coefficient')
plt.title('Force Coefficients')
plt.legend()


plt.figure(3, figsize=(8, 6))
# plt.plot(np.abs(cl_fft))
plt.plot(frequency, 2*np.abs(cl_fft)/n_samples)
plt.show()
