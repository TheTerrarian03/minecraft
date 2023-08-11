import numpy as np
import math


def find_min(values):
    return min(values)

def find_max(values):
    return max(values)

def find_midline(values):
    return (find_max(values) + find_min(values)) / 2

def find_amplitude(values):
    return (find_max(values) - find_min(values)) / 2

def find_period(values):
    return (2 * math.pi) / len(values)

def format_eq_for_x(points, amplitude, midline, period, x):
    h = find_h_for_x(points, amplitude, midline, period, x)

    eq = f"y = {round(amplitude, 3)} sin({round(period, 3)}x - {round(h, 3)}) + {midline}"

    return eq

# function to solve for h given other values
def find_h_for_x(points, amplitude, midline, period, x):
    y = points[x]
    h = ((math.asin((y - midline) / amplitude)) - (period * x))
    return h

# function to solve equation and return y points
def solve_eq_for_x(points, amplitude, midline, period, x):
    h = find_h_for_x(points, amplitude, midline, period, x)

    # Generate x-values from 0 to 12 with a step size of 0.01
    x = np.arange(0, len(points), 1)

    # Generate y-values using the sine function with the specified amplitude, midline, and period
    y = amplitude * -np.sin(((2 * np.pi / period) * x) - h) + midline

    return y

def find_all_possible_equations_solves(points, amplitude, midline, period):
    eqs = []
    
    for i in range(0, len(points)):
        solved_y_vals = solve_eq_for_x(points, amplitude, midline, period, i)
        eqs.append(solved_y_vals)
    
    return eqs

def find_best_x_worst_x(points, amplitude, midline, period):
    all_eqs = {key: [y_vals, 0] for key, y_vals in enumerate(find_all_possible_equations_solves(points, amplitude, midline, period))}

    for index in range(len(all_eqs)):
        eq_tuple = all_eqs[index]
        eq = eq_tuple[0]
        total_diff = 0

        for x_value in range(0, len(points)):
            total_diff += abs(points[x_value] - eq[x_value])
        
        # print(f"Difference for equation based on x-val #{index}: {total_diff}")
        all_eqs[index][1] = total_diff
    
    best_x = min(enumerate(all_eqs.values()), key=lambda x: x[1][1])[0]
    worst_x = max(enumerate(all_eqs.values()), key=lambda x: x[1][1])[0]

    # print(all_eqs)
    # print(best_x, worst_x)

    return best_x, worst_x