def calculate_energy_kwh(power_watts:float,minutes:int=15)->float:
    return(power_watts*(minutes/60.0))/1000.0