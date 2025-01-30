import matplotlib.pyplot as plt
import os
from config.settings import colors, markers, linestyles, DPI, SAVE_FORMATS, bar_width as global_bar_width , figsize as global_figsize, title_req

# Function to save the plot in different formats
def save_plot(fig, filename, folder):
    """Save a plot in multiple formats."""
    os.makedirs(folder, exist_ok=True)
    for fmt in SAVE_FORMATS:
        fig.savefig(f"{folder}/100_{filename}.{fmt}", dpi=DPI, bbox_inches='tight')

def plot_line_comparison(df, columns, labels, xlabel, ylabel, title, filename, folder):
    """
    Plot a line comparison graph for multiple columns and save it.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        columns (list): List of column names to plot.
        labels (list): List of labels for the legend corresponding to the columns.
        xlabel (str): Label for the X-axis.
        ylabel (str): Label for the Y-axis.
        title (str): Title of the plot.
        filename (str): Name of the file to save the plot.
        folder (str): Folder where the plot will be saved.
        formats (list): List of formats to save the plot.
        dpi (int): DPI resolution for the saved plot.
    """
    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#ff6347']  # Add more colors as needed
    # markers = ['o', 's', 'D', '^', 'v', 'p', '*', 'x']       # Add more markers as needed
    # linestyles = ['-', '--', '-.', ':']                      # Add more linestyles as needed

    fig, ax = plt.subplots(figsize=(4, 3))

    for i, (column, label) in enumerate(zip(columns, labels)):
        color = colors[i % len(colors)]
        marker = markers[i % len(markers)]
        linestyle = linestyles[i % len(linestyles)]
        ax.plot(df.index, df[column], color=color, marker=marker, linestyle=linestyle, label=label)

    if not title_req:
        title = ""
        
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    save_plot(fig, filename, folder)
    plt.close(fig)

def cdf_plot_line_comparison(df, index_rows, columns, labels, xlabel, ylabel, title, filename, folder):
    """
    Plot a line comparison graph for multiple columns and save it.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        columns (list): List of column names to plot.
        labels (list): List of labels for the legend corresponding to the columns.
        xlabel (str): Label for the X-axis.
        ylabel (str): Label for the Y-axis.
        title (str): Title of the plot.
        filename (str): Name of the file to save the plot.
        folder (str): Folder where the plot will be saved.
        formats (list): List of formats to save the plot.
        dpi (int): DPI resolution for the saved plot.
    """
    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#ff6347']  # Add more colors as needed
    # markers = ['o', 's', 'D', '^', 'v', 'p', '*', 'x']       # Add more markers as needed
    # linestyles = ['-', '--', '-.', ':']                      # Add more linestyles as needed

    fig, ax = plt.subplots(figsize=(4, 3))

    for i, (column, label) in enumerate(zip(columns, labels)):
        color = colors[i % len(colors)]
        marker = markers[i % len(markers)]
        linestyle = linestyles[i % len(linestyles)]
        ax.plot(df[index_rows], df[column], color=color, marker=marker, linestyle=linestyle, label=label)

    if not title_req:
        title = ""
        
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    save_plot(fig, filename, folder)
    plt.close(fig)


def plot_box_comparison(df, columns, labels, ylabel, title, filename, folder):
    """
    Plot a box comparison graph and save it, with custom colors for each box.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        columns (list): List of column names to include in the box plot.
        labels (list): List of labels corresponding to the columns.
        ylabel (str): Label for the Y-axis.
        title (str): Title of the plot.
        filename (str): Name of the file to save the plot.
        folder (str): Folder where the plot will be saved.
        formats (list): List of formats to save the plot.
        dpi (int): DPI resolution for the saved plot.
    """
    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#ff6347']  # Add more colors as needed
    
    fig, ax = plt.subplots(figsize=(4, 3))

    # Boxplot
    box = ax.boxplot(
        [df[col] for col in columns], 
        positions=range(1, len(columns) + 1), 
        widths=0.3, 
        patch_artist=True
    )

    # Apply colors to each box
    for patch, color in zip(box['boxes'], colors[:len(columns)]):
        patch.set_facecolor(color)
        patch.set_edgecolor('black')
    
    if not title_req:
        title = ""

    ax.set(
        title=title, 
        ylabel=ylabel, 
        xticks=range(1, len(labels) + 1), 
        xticklabels=labels
    )
    ax.grid(True)

    plt.tight_layout()
    save_plot(fig, filename, folder)
    plt.close(fig)

