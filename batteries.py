import matplotlib.pyplot as plt
import numpy as np

# Define the battery data
batteries = {
    "Nickel-Hydrogen": {
        'Grav_eng_dens': 65,  # Wh/kg
        'Vol_eng_dens': 52,  # Wh/dm³
        'Vch': 1.50,  # V
        'Vdis': 1.25,  # V
        'Vmax': 1.56,  # V
        'DOD': 0.35,  # %
        'Cycles': 40e3  # cycles
    },
    "Nickel-Cadmium": {
        'Grav_eng_dens': 83,  # Wh/kg
        'Vol_eng_dens': 33,  # Wh/dm³
        'Vch': 1.45,  # V
        'Vdis': 1.25,  # V
        'Vmax': 1.45,  # V
        'DOD': 0.35,  # %
        'Cycles': 20e3  # cycles
    },
    "Silver-Zinc": {
        'Grav_eng_dens': 110,  # Wh/kg
        'Vol_eng_dens': 225,  # Wh/dm³
        'Vch': 1.92,  # V
        'Vdis': 1.62,  # V
        'Vmax': 2.0,  # V
        'DOD': 0.5,  # %
        'Cycles': 200  # cycles
    },
    "Lithium ion": {
        'Grav_eng_dens': 110,  # Wh/kg
        'Vol_eng_dens': 270,  # Wh/dm³
        'Vch': 4.1,  # V
        'Vdis': 3.75,  # V
        'Vmax': 4.2,  # V
        'DOD': 0.70,  # %
        'Cycles': 10e3  # cycles
    }
}

# Extract the names of the batteries
battery_names = list(batteries.keys())

# Extract data for radar plot
labels = ['Volumetric Energy \nDensity (Wh/dm³)', 'Gravimetric Energy \nDensity (Wh/kg)', 'Charging Voltage (V)', 'Discharging Voltage (V)', 'Maximum Voltage (V)', 'Depth of Discharge (%)', 'Cycle Life']
num_vars = len(labels)

# Function to convert values to a 0-1 scale for plotting
def scale_data(data, max_values):
    return [val / max_val for val, max_val in zip(data, max_values)]

# Max values for scaling (based on given data)
max_values = [
    270,  # Volumetric Energy Density (Wh/dm³)
    110,  # Gravimetric Energy Density (Wh/kg)
    4.2,  # Charging Voltage (V)
    3.75, # Discharging Voltage (V)
    4.2,  # Maximum Voltage (V)
    1.0,  # Depth of Discharge (%)
    40e3  # Cycle Life
]

# Prepare data for radar plot
data = {}
for battery in battery_names:
    battery_data = [
        batteries[battery]['Vol_eng_dens'],
        batteries[battery]['Grav_eng_dens'],
        batteries[battery]['Vch'],
        batteries[battery]['Vdis'],
        batteries[battery]['Vmax'],
        batteries[battery]['DOD'],
        batteries[battery]['Cycles']
    ]
    data[battery] = scale_data(battery_data, max_values)

# Create radar plot
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each battery
for battery in battery_names:
    values = data[battery]
    values += values[:1]  # Complete the loop
    ax.fill(angles, values, alpha=0.25)
    ax.plot(angles, values, linewidth=2, label=battery)

# Add labels and title
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)

# Adjust label positions
for label, angle in zip(ax.get_xticklabels(), angles):
    if angle == 0:
        label.set_horizontalalignment('left')
        label.set_verticalalignment('center')
    elif angle == np.pi / 2:
        label.set_horizontalalignment('center')
        label.set_verticalalignment('bottom')
    elif angle == np.pi:
        label.set_horizontalalignment('right')
        label.set_verticalalignment('center')
    elif angle == 3 * np.pi / 2:
        label.set_horizontalalignment('center')
        label.set_verticalalignment('top')
    else:
        label.set_horizontalalignment('center')
        label.set_verticalalignment('center')
        
ax.set_title("Battery Comparison for Space Mission", fontsize=16, fontstyle='oblique', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.show()