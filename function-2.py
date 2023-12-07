# Function to calculate the energy balance for a heat exchanger
def heat_exchanger_energy_balance(mass_flow, specific_heat, temp_in, temp_out):
    """
    Calculate the energy transferred in a heat exchanger.

    Parameters:
    - mass_flow: Mass flow rate (kg/s)
    - specific_heat: Specific heat capacity (J/kg.K)
    - temp_in: Inlet temperature (K)
    - temp_out: Outlet temperature (K)

    Returns:
    - energy_transfer: Energy transferred (J)
    """
    energy_transfer = mass_flow * specific_heat * (temp_out - temp_in)
    return energy_transfer

# Example values for two heat exchangers in series
mass_flow = 0.1  # Mass flow rate in kg/s
specific_heat = 4186  # Specific heat capacity of water in J/kg.K
temp_in_1 = 298  # Inlet temperature of first heat exchanger in K
temp_out_1 = 320  # Outlet temperature of first heat exchanger in K
temp_in_2 = temp_out_1  # Inlet temperature of second heat exchanger is the outlet temperature of the first
temp_out_2 = 340  # Outlet temperature of second heat exchanger in K

# Calculate the energy transferred in each heat exchanger
energy_transfer_1 = heat_exchanger_energy_balance(mass_flow, specific_heat, temp_in_1, temp_out_1)
energy_transfer_2 = heat_exchanger_energy_balance(mass_flow, specific_heat, temp_in_2, temp_out_2)

# The results are the energy transferred in each heat exchanger and their sum
print(f"Energy transferred in heat exchanger 1: {energy_transfer_1} J")
print(f"Energy transferred in heat exchanger 2: {energy_transfer_2} J")
print(f"Total energy transferred in both heat exchangers: {energy_transfer_1 + energy_transfer_2} J")
