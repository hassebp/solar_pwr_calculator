import numpy as np
import matplotlib.pyplot as plt

# Given values
P_t = 1000  # Transmitted power in watts
G_t = 10  # Transmitting antenna gain (linear scale)
G_r = 10  # Receiving antenna gain (linear scale)

# Speed of light
c = 3e8

wavelength = 0.03  # Wavelength in meters (10 GHz)
# Frequencies and corresponding wavelengths and gains (in dB)
frequencies = {
    '2.4 GHz': {'f': 2.4e9, 'G_dB': 20},
    '5 GHz': {'f': 5e9, 'G_dB': 20},
    '10 GHz': {'f': 10e9, 'G_dB': 20}
}

# Transmitted power in dB
P_t_dB = 10*np.log10(1000) + 30

# Distance range (1 meter to 100 meters)
R = np.linspace(1, 1000, 500)



# Plotting
plt.figure(figsize=(10, 6))

for label, params in frequencies.items():
    f = params['f']
    G_t_dB = G_r_dB = params['G_dB']
    wavelength = c / f
    
    # Received power in dB
    P_r_dB = P_t_dB + G_t_dB + G_r_dB + 20 * np.log10(wavelength / (4 * np.pi * R))
    
    plt.plot(R, P_r_dB, label=f'{label} (Gain={G_t_dB} dBi)')
    
plt.xlabel('Distance R (m)', fontsize=13)
plt.ylabel('Received Power $P_r$ (dB)',fontsize=13)
plt.title(f'Received Power vs Distance for Different Microwave Frequencies \n For transmitted power of {P_t_dB} dB',fontsize=15)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()