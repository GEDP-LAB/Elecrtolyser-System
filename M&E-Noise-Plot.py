import matplotlib.pyplot as plt
import numpy as np

def heat_exchanger_energy_balance(mass_flow, specific_heat, temp_in, temp_out):
    energy_transfer = mass_flow * specific_heat * (temp_out - temp_in)
    return energy_transfer

def heat_exchanger_material_balance(mass_flow_in, mass_flow_out):
    tolerance = 1e-5
    return abs(mass_flow_in - mass_flow_out) < tolerance

def complex_temperature_variation(initial_temp, final_temp, steps):
    x = np.linspace(0, 1, steps)
    y = np.sin(x * np.pi) * (final_temp - initial_temp) / 2 + (final_temp + initial_temp) / 2
    return y

mass_flow_in = 0.1  # kg/s
specific_heat = 4186  # J/kg.K
steps = 4

temp_in_1 = 298  # K
temp_out_1 = 320  # K
temp_in_2 = temp_out_1  # K
temp_out_2 = 340  # K

temp_profile_1 = complex_temperature_variation(temp_in_1, temp_out_1, steps)
temp_profile_2 = complex_temperature_variation(temp_in_2, temp_out_2, steps)

temperatures = np.concatenate(([temp_in_1], temp_profile_1, temp_profile_2, [temp_out_2]))
stages = ['Inlet'] + [f'Step {i+1}' for i in range(steps * 2)] + ['After Exchanger 2']

energy_transfer_1 = heat_exchanger_energy_balance(mass_flow_in, specific_heat, temp_in_1, temp_out_1)
energy_transfer_2 = heat_exchanger_energy_balance(mass_flow_in, specific_heat, temp_in_2, temp_out_2)

material_balance_correct = heat_exchanger_material_balance(mass_flow_in, mass_flow_out_2)

plt.figure(figsize=(12, 6))
plt.plot(stages, temperatures, marker='o')
plt.title('Complex Temperature Profile Across Heat Exchangers')
plt.xlabel('Stage')
plt.ylabel('Temperature (K)')
plt.grid(True)
plt.show()

print("Heat Exchanger 1:")
print(f"Inlet Temperature: {temp_in_1} K")
print(f"Outlet Temperature: {temp_out_1} K")
print(f"Mass Flow Rate: {mass_flow_in} kg/s")
print(f"Energy Transferred: {energy_transfer_1} J")
print("\nHeat Exchanger 2:")
print(f"Inlet Temperature: {temp_in_2} K")
print(f"Outlet Temperature: {temp_out_2} K")
print(f"Mass Flow Rate: {mass_flow_in} kg/s")
print(f"Energy Transferred: {energy_transfer_2} J")
print("\nOverall System:")
print(f"Total Energy Transferred: {energy_transfer_1 + energy_transfer_2} J")
print(f"Material Balance is {'correct' if material_balance_correct else 'incorrect'}")
