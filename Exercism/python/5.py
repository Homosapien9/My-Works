
def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature<800 and neutrons_emitted>500 and (temperature)*(neutrons_emitted)<500000:
        return True
    else :
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    Efficiency=(generated_power/ theoretical_max_power)*100
    if Efficiency>=80:
        return "green"
    elif Efficiency>=60 and Efficiency<80:
        return "orange"
    elif Efficiency>=30 and Efficiency<60:
        return "red"
    else:
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    calculation = temperature * neutrons_produced_per_second

    if calculation < 0.9 * threshold:
        return "LOW"
    elif calculation <= 1.1 * threshold:
        return "NORMAL"
    else:
        return "DANGER"
