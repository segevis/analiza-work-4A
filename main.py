# Group:
# Sapir Natanov 322378068
# Dor Maudi 207055138
# Noa Yasharzadeh 208595157
# Segev Isaac 207938085
import numpy as np


def linear_interpolation(x_values, y_values, x):
    # Check if the given x value is within the range of x_values
    if x < min(x_values) or x > max(x_values):
        return None  # Return None if x is outside the range of known data

    # Find the two nearest known x values
    x1 = max(val for val in x_values if val <= x)
    x2 = min(val for val in x_values if val >= x)

    # Find the corresponding y values
    y1 = y_values[x_values.index(x1)]
    y2 = y_values[x_values.index(x2)]

    # Perform linear interpolation
    y = y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)
    return y


def polynomial_interpolation(x_values, y_values, x):
    # Fit a polynomial of degree len(x_values) - 1 to the data
    coeffs = np.polyfit(x_values, y_values, len(x_values) - 1)

    # Evaluate the polynomial at the given x value
    y = np.polyval(coeffs, x)
    return y


def lagrange_interpolation(x_values, y_values, x):
    # Perform Lagrange interpolation
    n = len(x_values)
    y = 0
    for i in range(n):
        # Calculate the Lagrange basis polynomial for the ith point
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        y += term
    return y


if __name__ == '__main__':
    # Example data
    x_values = [0, 1, 2, 3, 4]
    y_values = [0, 1, 4, 9, 16]

    # Good examples:
    # Linear interpolation
    interpolated_value = linear_interpolation(x_values, y_values, 2.5)
    print("Linear Interpolated value at x = 2.5 (Good example):", interpolated_value)

    # Polynomial interpolation
    interpolated_value = polynomial_interpolation(x_values, y_values, 2.5)
    print("Polynomial Interpolated value at x = 2.5 (Good example):", interpolated_value)

    # Lagrange interpolation
    interpolated_value = lagrange_interpolation(x_values, y_values, 2.5)
    print("Lagrange Interpolated value at x = 2.5 (Good example):", interpolated_value)

    # Bad examples:
    # Linear interpolation - Interpolating outside the range of known data
    interpolated_value = linear_interpolation(x_values, y_values, 5)
    print("Linear Interpolated value at x = 5 (Bad example):", interpolated_value)

    # Polynomial interpolation - No bad example as polynomial interpolation can extrapolate
    # Lagrange interpolation - No bad example as Lagrange interpolation can extrapolate
