import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Concentration ratio range
concentration_ratio = np.linspace(1, 1500, 100)

# General efficiency functions based on typical behaviors and published data
def parabolic_trough_efficiency(concentration_ratio):
    return (0.14 + (0.20 - 0.14) * (1 - np.exp(-0.0005 * concentration_ratio))) * 100

def linear_fresnel_efficiency(concentration_ratio):
    return 0.18 * np.ones_like(concentration_ratio) * 100

def solar_tower_efficiency(concentration_ratio):
    return (0.23 + (0.35 - 0.23) * (1 - np.exp(-0.0007 * concentration_ratio))) * 100

def parabolic_dish_efficiency(concentration_ratio):
    return 0.30 * np.ones_like(concentration_ratio) * 100

# Create efficiency plots
plt.figure(figsize=(10, 6))

sns.lineplot(x=concentration_ratio, y=parabolic_trough_efficiency(concentration_ratio), label='Parabolic Trough')
sns.lineplot(x=concentration_ratio, y=linear_fresnel_efficiency(concentration_ratio), label='Linear Fresnel')
sns.lineplot(x=concentration_ratio, y=solar_tower_efficiency(concentration_ratio), label='Solar Tower')
sns.lineplot(x=concentration_ratio, y=parabolic_dish_efficiency(concentration_ratio), label='Parabolic Dish')

plt.xlabel('Concentration Ratio', fontsize=13)
plt.ylabel('Efficiency [%]', fontsize=13)
plt.title('Efficiency vs. Concentration Ratio for Different Heliostat Systems', fontsize=15)
plt.legend(fontsize=10)
plt.show()

# Constants
solar_constant = 1361  # Solar constant in W/m^2

# Collector area range (example range from 100 to 50,000 square meters)
collector_area = np.linspace(0, 500, 50)

# Efficiency values for different systems
parabolic_trough_efficiency_value = 0.17  # Average efficiency
linear_fresnel_efficiency_value = 0.18  # Constant efficiency
solar_tower_efficiency_value = 0.35  # Average efficiency
parabolic_dish_efficiency_value = 0.30  # Constant efficiency

# Energy output calculation (Efficiency * Solar constant * Collector area)
parabolic_trough_output = parabolic_trough_efficiency_value * solar_constant * collector_area
linear_fresnel_output = linear_fresnel_efficiency_value * solar_constant * collector_area
solar_tower_output = solar_tower_efficiency_value * solar_constant * collector_area
parabolic_dish_output = parabolic_dish_efficiency_value * solar_constant * collector_area

# Create energy output plots
plt.figure(figsize=(10, 6))

sns.lineplot(x=collector_area, y=parabolic_trough_output / 1e3, label='Parabolic Trough')
sns.lineplot(x=collector_area, y=linear_fresnel_output / 1e3, label='Linear Fresnel')
sns.lineplot(x=collector_area, y=solar_tower_output / 1e3, label='Solar Tower')
sns.lineplot(x=collector_area, y=parabolic_dish_output / 1e3, label='Parabolic Dish')

plt.xlabel('Collector Area ($m^2$)', fontsize=13)
plt.ylabel('Energy Output (kW)', fontsize=13)
plt.title('Energy Output vs. Collector Area for Different Heliostat Systems', fontsize=15)
plt.legend(fontsize=10)
plt.show()