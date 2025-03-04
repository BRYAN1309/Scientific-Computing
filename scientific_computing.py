# -*- coding: utf-8 -*-
"""Scientific Computing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Sif8GGXqKF57eYZ99y2HiNcLKhxTjSLG
"""

import numpy as np

def my_num_calc(f, a, b, n, option):
    # Ensure n is odd as required by Simpson's rule
    if n % 2 == 0:
        raise ValueError("n must be odd")

    # Calculate the width of each subinterval
    h = (b - a) / (n - 1)

    # Generate the grid of n evenly spaced points
    x = np.linspace(a, b, n)

    if option == "rect":
        # Right endpoint rectangle method
        I = sum(f(x[i]) * h for i in range(1, n))

    elif option == "trap":
        # Trapezoidal method
        I = (f(a) + f(b)) / 2
        I += sum(f(x[i]) for i in range(1, n-1))
        I *= h

    elif option == "simp":
        # Simpson's rule
        I = f(a) + f(b)
        for i in range(1, n-1):
            if i % 2 == 0:
                I += 2 * f(x[i])
            else:
                I += 4 * f(x[i])
        I *= h / 3

    else:
        raise ValueError("Unknown option for integration method")

    return I

In: my_numint(f, 0, 1, 3, "trap")