#/utils/plotter.py
import matplotlib.pyplot as plt
import os
import itertools

from config.settings import colors, markers, linestyles, DPI, SAVE_FORMATS, bar_width as global_bar_width , figsize as global_figsize, title_req


# Color, marker, and linestyle options
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#ff6347']  # Add more colors as needed
markers = ['o', 's', 'D', '^', 'v', 'p', '*', 'x']         # Add more markers as needed
linestyles = ['-', '--', '-.', ':']                         # Add more linestyles as needed

# Function to save the plot in different formats
def save_plot(fig, filename, folder):
    """Save a plot in multiple formats."""
    os.makedirs(folder, exist_ok=True)
    for fmt in SAVE_FORMATS:
        fig.savefig(f"{folder}/{filename}.{fmt}", dpi=DPI, bbox_inches='tight')

# Function to plot metrics with color, marker, and linestyle cycling
def plot_metric(df, x_column, y_columns, labels, title, xlabel, ylabel, filename, folder):
    """Plot one or more metrics."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=DPI)
    
    # Create iterators for cycling through colors, markers, and linestyles
    color_cycle = itertools.cycle(colors)
    marker_cycle = itertools.cycle(markers)
    linestyle_cycle = itertools.cycle(linestyles)
    
    for y_column, label in zip(y_columns, labels):
        # Get the next available color, marker, and linestyle
        color = next(color_cycle)
        marker = next(marker_cycle)
        linestyle = next(linestyle_cycle)
        
        # Plot the line with chosen style and color
        ax.plot(
            df[x_column], df[y_column], 
            label=label, 
            color=color, 
            marker=marker, 
            linestyle=linestyle
        )
    if not title_req:
        title = ""
    # Set plot properties
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.legend()
    ax.grid(True)
    
    # Tight layout and save the plot
    plt.tight_layout()
    save_plot(fig, filename, folder)
    plt.close(fig)


# Function to plot multiple datasets for comparison
def plot_comparison(dfs, x_column, y_column, labels, title, xlabel, ylabel, filename, folder):
    """Compare multiple datasets on a single plot."""
    fig, ax = plt.subplots(figsize=(6, 4), dpi=DPI)
    
    # Create iterators for cycling through colors, markers, and linestyles
    color_cycle = itertools.cycle(colors)
    marker_cycle = itertools.cycle(markers)
    linestyle_cycle = itertools.cycle(linestyles)
    
    for df, label in zip(dfs, labels):
        # Get the next available color, marker, and linestyle
        color = next(color_cycle)
        marker = next(marker_cycle)
        linestyle = next(linestyle_cycle)
        
        # Plot the line with chosen style and color
        ax.plot(
            df[x_column], df[y_column], 
            label=label, 
            color=color, 
            marker=marker, 
            linestyle=linestyle
        )

    if not title_req:
        title = ""

    # Set plot properties
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.legend()
    ax.grid(True)
    
    # Tight layout and save the plot
    plt.tight_layout()
    print("folder save", folder)
    save_plot(fig, filename, folder)
    plt.close(fig)

