import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Solid mechanics calculations for trocar prototypes.
'''

# Calculate the deflection and elastic curve for cantilevered beam due to a force P on the end (Hibbeler solids 10th ed., p. 815, first diagram from the top)
def force_deflect(I, L, P, E):
    """
    Calculate the deflection and elastic curve for a cantilevered beam due to a force P on the end.

    Parameters:
    I (float): Moment of inertia of the section.
    L (float): Length of the beam.
    P (float): Force applied on the end of the beam.
    E (float): Modulus of elasticity of the material.
    x (float): Distance from the fixed end.

    Returns:
    tuple: Maximum deflection angle, maximum deflection, deflection at distance x.
    """
    
    v_max = (-P * L**3) / (3*E*I)
    
    theta_max_deg = (- P * L**2) / (2*E*I) * (180 * np.pi)

    df = pd.DataFrame({
        'Force (N)': forces,
        'Displacement (cm)': v_max*100,
        'Angular Deflection (deg.)': theta_max_deg
    })

    return df

# Calculate the deflection and elastic curve for cantilevered beam due to couple moment M_0 on the end (Hibbeler solids 10th ed., p. 815, fourth diagram from the top)
def moment_deflect(I, L, E, M_0):
    """
    Calculate the deflection and elastic curve for a cantilevered beam due to a couple moment M_0 on the end.

    Parameters:
    I (float): Moment of inertia of the section.
    L (float): Length of the beam.
    E (float): Modulus of elasticity of the material.
    M_0 (float): Couple moment on the end of the beam.
    x (float): Distance from the fixed end.

    Returns:
    tuple: Maximum deflection angle, maximum deflection, deflection at distance x.
    """
    
    theta_max = (M_0*L) / (E*I)

    v_max = (M_0 * L**2) / (2*E*I)

    return v_max, theta_max

def plot(df, title):
    plt.plot(df.iloc[:, 0], df.iloc[:, 1], 'r')
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.title(title)
    plt.show()
    plt.savefig(title.lower().replace(" ", "_")+'_disp.png', dpi=1000)

    plt.plot(df.iloc[:, 0], df.iloc[:, 2], 'b')
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[2])
    plt.title(title)
    plt.show()
    plt.savefig(title.lower().replace(" ", "_")+'_ang_disp.png', dpi=1000)

# Young's Moduli
clear_young = 2080 * 1000000
durable_young = 994 * 1000000
white_young = 2020.16 * 1000000

# Moment of inertia calculations assuming tubular circular area
d_mm_outer = 4.5 # For the double balloon
d_mm_inner = 3.5 # For the double balloon

d_m_outer = d_mm_outer / 1000
d_m_inner = d_mm_inner / 1000

I = np.pi*(d_m_outer**4 - d_m_inner**4) / 64 # I_x = I_y = I

L_mm = 145 # For the double balloon
L = L_mm / 1000
    
forces = np.linspace(0, 50, 10000)

clear_biomed = force_deflect(I=I, L=L, P=forces, E=clear_young)
clear_biomed.to_csv('clear_biomed.csv', index=False)

durable_biomed = force_deflect(I=I, L=L, P=forces, E=durable_young)
durable_biomed.to_csv('durable_biomed.csv', index=False)

white_biomed = force_deflect(I=I, L=L, P=forces, E=white_young)
white_biomed.to_csv('white_biomed.csv', index=False)

plot(clear_biomed, title='Clear BioMed Resin')