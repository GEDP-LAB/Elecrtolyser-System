import matplotlib.pyplot as plt

# Function to calculate the energy balance for a heat exchanger
def heat_exchanger_energy_balance(mass_flow, specific_heat, temp_in, temp_out):
    energy_transfer = mass_flow * specific_heat * (temp_out - temp_in)
    return energy_transfer

# Function to calculate the material balance for a heat exchanger
def heat_exchanger_material_balance(mass_flow_in, mass_flow_out):
    tolerance = 1e-5
    return abs(mass_flow_in - mass_flow_out) < tolerance

# Example values for two heat exchangers in series
mass_flow_in = 0.1  # kg/s
specific_heat = 4186  # J/kg.K
temp_in_1 = 298  # K
temp_out_1 = 320  # K
temp_in_2 = temp_out_1  # K
temp_out_2 = 340  # K
mass_flow_out_2 = mass_flow_in  # Assuming no mass loss

# Calculate the energy transferred in each heat exchanger
energy_transfer_1 = heat_exchanger_energy_balance(mass_flow_in, specific_heat, temp_in_1, temp_out_1)
energy_transfer_2 = heat_exchanger_energy_balance(mass_flow_in, specific_heat, temp_in_2, temp_out_2)

# Verify the material balance for the system
material_balance_correct = heat_exchanger_material_balance(mass_flow_in, mass_flow_out_2)

# Plotting the temperature profile
temperatures = [temp_in_1, temp_out_1, temp_out_2]
stages = ['Inlet', 'After Exchanger 1', 'After Exchanger 2']

plt.figure(figsize=(10, 6))
plt.plot(stages, temperatures, marker='o')
plt.title('Temperature Profile Across Heat Exchangers')
plt.xlabel('Stage')
plt.ylabel('Temperature (K)')
plt.grid(True)
plt.show()

# Print the detailed results
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
