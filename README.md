# Port Calculations

Calculations for the 3mm port with Children's Hospital Colorado. Senior design 2023-2024.

References:

Hibbeler, Russell C. *Mechanics of Materials*. 10th ed., Pearson, 2017.

## Code Structure - `solids_calcs.py`

The file that needs to be run is `solid_calcs.py`. It requires several inputs from the user as follows:

`d_mm_outer`: User-entered outer diameter in millimeters (mm).

`d_mm_inner`: User-entered inner diameter in millimeters (mm).

`L_mm_outer`: User-entered trocar length in millimeters (mm).

`P`: User-entered applied force in Newtons (N), assuming that it is on the end of the trocar.

`E_mpa`: User-entered Young's modulus/modulus of elasticity in megapascals (MPa).

`M_0`: User-entered couple moment (i.e. pure moment, **not** a moment due to a force) in Newton-meters (N*m).

The code then calculates the area moment of inertia, or second moment of inertia, according to $I = \frac{ \pi }{ 64 } \left( d_o^4 - d_i^4 \right)$, where $d_o$ and $d_i$ are the outer and inner diameters in meters, respectively. Also note that $I_x = I_y = I$.

This information is then passed to two functions, `force_deflect` and `moment_deflect`.


## Description - `force_deflect`

`force_deflect` takes the following as inputs:

* I
* L
* P
* E
* x
  
It then uses equations for the angular and length displacement from beam tables for a cantilevered beam with a force $P$ on the end to calculate the maximum deflection (both angular and displacement). It also returns the elastic curve to be plotted later.

## Description - `moment_deflect`

`moment_deflect` takes the following as inputs:

* I
* L
* E
* M_0
* x
  
It then uses equations for the angular and length displacement from beam tables for a cantilevered beam with a couple moment on the end to calculate the maximum deflection (both angular and displacement). It also returns the elastic curve to be plotted later.

The code under `## Elastic curve plots` plots the resulting elastic curves from earlier. To save the figures, uncomment the following lines by deleting the `#` symbol:

```python
# plt.savefig('force_elastic_curve', dpi=1000)
# plt.savefig('moment_elastic_curve', dpi=1000)
```

## Code Structure - `solids_calcs_online.ipynb`

`solids_calcs_online.ipynb` does the exact same math as `solids_calcs.py`, the only difference being that in `solids_calcs_online.ipynb` you have to manually type in the parameters before running the code (exactly like a MatLab script). It also runs in the cloud with [Google Colab](https://colab.research.google.com/), so you don't need Python on your computer. What you edit is at the top of the document with a comment next to it saying ''Edit this line'' and a description of what the variable represents. The code handles the rest.
