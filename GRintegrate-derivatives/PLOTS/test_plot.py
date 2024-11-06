#!/usr/bin/env python
import os
import numpy as np
import skfda
from skfda.preprocessing.smoothing import BasisSmoother
from skfda.representation.basis import FourierBasis
import matplotlib.pyplot as plt

# Example data resembling the blue line trend
x = np.linspace(0, 10, 50)  # x values
y = 12 - 2 * np.exp(-x / 3) + np.random.normal(0, 0.02, x.size)  # y values approaching zero from above

# Define a Fourier basis for smoothing
basis = FourierBasis(domain_range=(0, 10), n_basis=5)
fd_data = skfda.FDataGrid(data_matrix=y[:, np.newaxis], grid_points=x)

# Apply the basis smoother for extrapolation
smoother = BasisSmoother(basis=basis)
smoothed_fd = smoother.fit_transform(fd_data)

# Extrapolate by evaluating the smoothed function at points beyond the data
x_extrapolated = np.linspace(0, 12, 60)  # Extended x range for extrapolation
y_extrapolated = smoothed_fd(x_extrapolated)

# Plot the original data and extrapolation
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label="Original Data")
plt.plot(x_extrapolated, y_extrapolated, color='red', label="Extrapolated Fit")
plt.axhline(0, color='gray', linestyle='--', label="y=0")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Extrapolation to Zero with skfda (Decreasing Trend)")

output_dir = os.getcwd()
file_name = f"test_extrapolation.jpg"
file_path = os.path.join(output_dir, file_name)
plt.savefig(file_path, dpi=1200, bbox_inches='tight')
plt.savefig(fr"{file_name}", dpi=1200, bbox_inches='tight')