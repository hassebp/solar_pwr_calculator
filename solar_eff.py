import numpy as np

# Constants
q = 1.602e-19  # Elementary charge (C)
k = 1.381e-23  # Boltzmann constant (J/K)

# Given parameters
I_SC = 5.0  # Short-circuit current (A)
I_O = 1e-12  # Reverse saturation current (A)
V = 0.6  # Voltage (V)
A = 1.0  # Diode ideality factor

# Define temperature range in Celsius
T_celsius = np.linspace(-173, 106, 100)

# Convert Celsius to Kelvin
T_kelvin = T_celsius + 273.15

# Normalize temperature to range [0, 1]
T_norm = (T_kelvin - (273.15 - 173)) / (106 + 173 - (273.15 - 173))

# Current equation
I_L = I_SC - I_O * (np.exp(q * V / (A * k * T_kelvin)) - 1)

# Calculate efficiency
efficiency = I_L / I_SC

# Plotting
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(T_celsius, efficiency * 100, color='blue')
plt.title('Efficiency vs. Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Efficiency (%)')
plt.grid(True)
plt.show()