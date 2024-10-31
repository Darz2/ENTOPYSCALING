#!/usr/bin/env python
import numpy as np

Nbin = 20000
Delta = 0.01
Twopi = 8.0 * np.arctan(1.0)
Gamma = [2,5,10,15,20]

def glng(x):
    if x < 1.0e-20:
        return 0.0
    else:
        return x * np.log(x)
    

for j in Gamma:
    
    with open(f'gr_{j}.txt', 'w') as f1, open(f'ggr_5.{j}', 'w') as f2:
        for i in range(1, Nbin + 1):
            R = (float(i) - 0.5) * Delta
            
            if R < 0.95:
                G = 0.0
            else:
                G = 1.0 + 1.5 * np.exp((1.0 - R) / j) * np.cos(Twopi * (R - 1.05)) / R

            f1.write(f"{R:.6f} {G:.6f}\n")

            f2.write(f"{R:.6f} {1.0 - G:.6f} {glng(G) + 1.0 - G:.6f}\n")
