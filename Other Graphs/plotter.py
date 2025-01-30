import matplotlib.pyplot as plt
import os
from config.settings import colors, DPI, SAVE_FORMATS, bar_width as global_bar_width , figsize as global_figsize, title_req
import seaborn as sns
import numpy as np
# Set plotting style
sns.set_style("darkgrid")

# Function to save the plot in different formats
def save_plot(fig, filename, folder):
    """Save a plot in multiple formats."""
    os.makedirs(folder, exist_ok=True)
    for fmt in SAVE_FORMATS:
        fig.savefig(f"{folder}/{filename}.{fmt}", dpi=DPI, bbox_inches='tight')


# Function to create bar plots
def plot_bar(data,labels, ylabel,title, filename, folder, colors=colors, bar_width=global_bar_width, figsize=global_figsize):
    """Create a bar plot for given labels and data."""
    positions = np.arange(len(labels))

    # Initialize the plot
    fig, ax = plt.subplots(figsize=figsize, dpi=DPI)

    # Create the bars
    bars = ax.bar(positions, data, width=bar_width, color=colors or 'blue')

    # Add value annotations
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.005 * max(data), f"{yval:.4f}", 
                ha='center', va='bottom')
        
    if not title_req:
        title = ""

    # Set labels and ticks
    ax.set_ylabel(ylabel)
    ax.set_xticks(positions)
    ax.set_xticklabels(labels, rotation=15)
    ax.set_title(title)
    ax.grid(True)

    # Remove unnecessary spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Adjust layout and save plot
    plt.tight_layout()
    save_plot(fig, filename, folder)
    plt.close(fig)



import matplotlib.pyplot as plt
import numpy as np

# Function to create bar plots
def plot_bar_adjust(data, labels, ylabel, title, filename, folder, colors=colors, bar_width=global_bar_width, figsize=global_figsize):
    """Create a bar plot for given labels and data."""
    positions = np.arange(len(labels))

    # Split labels into multiple lines if they are too long
    max_label_length = 20  # Set a threshold for label length
    wrapped_labels = []
    for label in labels:
        if len(label) > max_label_length:
            # Wrap the label into multiple lines
            words = label.split(' ')
            wrapped_label = ''
            current_line = ''
            for word in words:
                # If the current line plus the new word exceeds max length, start a new line
                if len(current_line + word) > max_label_length:
                    wrapped_label += current_line + '\n'
                    current_line = word + ' '
                else:
                    current_line += word + ' '
            wrapped_label += current_line  # Add the remaining part of the label
            wrapped_labels.append(wrapped_label.strip())
        else:
            wrapped_labels.append(label)

    # Initialize the plot
    fig, ax = plt.subplots(figsize=figsize, dpi=DPI)

    # Create the bars
    bars = ax.bar(positions, data, width=bar_width, color=colors or 'blue')

    # Add value annotations
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.005 * max(data), f"{yval:.4f}", 
                ha='center', va='bottom')
        
    if not title_req:
        title = ""

    # Set labels and ticks
    ax.set_ylabel(ylabel)
    ax.set_xticks(positions)
    ax.set_xticklabels(wrapped_labels, rotation=15)
    ax.set_title(title)
    ax.grid(True)

    # Remove unnecessary spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Adjust layout and save plot
    plt.tight_layout()
    save_plot(fig, filename, folder)
    plt.close(fig)
