import matplotlib.pyplot as plt
import calculations

# hex codes for important line colors
class COLORS:
    POINT = "#000000"
    MAX = "#ff0000"
    MIN = "#0088ff"
    MIDLINE = "#ffd800"
    BEST = "#06d611"
    WORST = "#6f00bf"

# graph to find values and export graph to png
def export_graph(y_coords, title="Data", x_label="x", y_label="y", output_file="data_graph.png"):
    x_coords  = list(range(len(y_coords)))
    min_val   = calculations.find_min(y_coords)
    max_val   = calculations.find_max(y_coords)
    midline   = calculations.find_midline(y_coords)
    amplitude = calculations.find_amplitude(y_coords)
    period    = calculations.find_period(y_coords)

    best_x, worst_x = calculations.find_best_x_worst_x(y_coords, amplitude, midline, period)

    plot_attributes(min_val, max_val, midline)
    plot_scatter(x_coords, y_coords)
    plot_accurate_estimate(best_x, y_coords, amplitude, midline, period)
    plot_inaccurate_estimates(best_x, worst_x, y_coords, amplitude, midline, period)
    plot_most_inaccurate_estimate(worst_x, y_coords, amplitude, midline, period)

    setup_labels(title, x_label, y_label)

    add_best_worst_text(best_x, worst_x)

    plt.savefig(output_file)

    close_plot()

    # return best eq
    return calculations.format_eq_for_x(y_coords, amplitude, midline, period, best_x)

# function to setup plot labels
def setup_labels(title="Data", x_label="x", y_label="y"):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(["Max Value", "Min Value", "Midline", "Original Points", "Best Sine Est", "Worst Sine Est"])

def add_best_worst_text(best_x, worst_x):
    plt.text(plt.gca().get_xlim()[0]+1.75, plt.gca().get_ylim()[0]-4, f"Best est x value: {best_x}", ha='center', va='center', color='red')
    plt.text(plt.gca().get_xlim()[1]-1.75, plt.gca().get_ylim()[0]-4, f"Worst est x value: {worst_x}", ha='center', va='center', color='blue')

# function to plot knowns- min, max, midline, and points
def plot_attributes(min_val, max_val, midline):
    plt.axhline(max_val, color=COLORS.MAX)
    plt.axhline(min_val, color=COLORS.MIN)
    plt.axhline(midline, color=COLORS.MIDLINE)

def plot_scatter(x_coords, y_coords):
    plt.scatter(x_coords, y_coords, c=COLORS.POINT)

# function to plot all other inaccurate estimates- 0.4 opacity
def plot_inaccurate_estimates(best_x, worst_x, y_coords, amplitude, midline, period):
    for i in range(0, len(y_coords)):
        if (i != best_x) and (i != worst_x):
            eq = calculations.solve_eq_for_x(y_coords, amplitude, midline, period, i)
            plt.plot(eq, linestyle="dashdot", alpha = 0.4)

# function to plot most accurate estimage
def plot_accurate_estimate(best_x, y_coords, amplitude, midline, period):
    eq = calculations.solve_eq_for_x(y_coords, amplitude, midline, period, best_x)
    plt.plot(eq, linewidth=2.5, c=COLORS.BEST)

def plot_most_inaccurate_estimate(worst_x, y_coords, amplitude, midline, period):
    eq = calculations.solve_eq_for_x(y_coords, amplitude, midline, period, worst_x)
    plt.plot(eq, linestyle="dashdot", c=COLORS.WORST)

# function to clear and close plot
def close_plot():
    plt.close()