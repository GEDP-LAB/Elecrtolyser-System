def energy_balance(mass_flow, specific_heat, temperature_in, temperature_out):
    """
    Calculate the energy transfer in a heat exchanger.

    Parameters:
    - mass_flow: Mass flow rate (kg/h)
    - specific_heat: Specific heat capacity (kJ/kg.K)
    - temperature_in: Inlet temperature (C)
    - temperature_out: Outlet temperature (C)

    Returns:
    - Energy transfer in kJ/h
    """
    energy_transfer = mass_flow * specific_heat * (temperature_out - temperature_in)
    return energy_transfer

# Example usage for a cooling process:
mass_flow = 100.0  # Mass flow rate in kg/h
specific_heat = 4.18  # Specific heat capacity of water in kJ/kg.K
temperature_in = 100.0  # Inlet temperature in C
temperature_out = 60.0  # Outlet temperature in C

energy_transfer = energy_balance(mass_flow, specific_heat, temperature_in, temperature_out)
print(f"The energy transfer in the heat exchanger is {energy_transfer} kJ/h")
