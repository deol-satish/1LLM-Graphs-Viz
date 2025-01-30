import os
from utils.data_loader import load_log_files, parse_logs
from utils.plotter import plot_comparison
from config.settings import GRAPH_SAVE_FOLDER, DATA_FOLDER, SAVE_FORMATS

llm_tags = ['opt_train', 'gpt_train', 't5llm_train', 'llama_train1', 'llama_train2', 'llama_train3']
label_name = "Training"

# Create a list to store dataframes for comparison
dfs = []
labels = []

for llm_tag in llm_tags:
    # Paths
    log_dir = os.path.join(DATA_FOLDER, llm_tag)
    print(log_dir, label_name)
    
    # Load and process data
    log_files = load_log_files(log_dir, label_name)
    df = parse_logs(log_dir, log_files, label_name)
    
    # Append the dataframe and label
    dfs.append(df)
    labels.append(llm_tag)

# Ensure the save folder exists
os.makedirs(GRAPH_SAVE_FOLDER, exist_ok=True)

# Save folder for comparison plots
comparison_folder = os.path.join(GRAPH_SAVE_FOLDER, label_name+"comparison")
os.makedirs(comparison_folder, exist_ok=True)

# Plot Mean Loss comparison
plot_comparison(
    dfs, 'Epoch', 'Mean Loss', labels,
    'Mean Loss Comparison over Epochs', 'Epoch', 'Mean Loss',
    "Mean_Loss_Comparison", comparison_folder
)

# Plot Mean Accuracy comparison
plot_comparison(
    dfs, 'Epoch', 'Mean Accuracy', labels,
    'Mean Accuracy Comparison over Epochs', 'Epoch', 'Mean Accuracy',
    "Mean_Accuracy_Comparison", comparison_folder
)




import os
from utils.data_loader import load_log_files, parse_logs
from utils.plotter import plot_comparison
from config.settings import GRAPH_SAVE_FOLDER, DATA_FOLDER, SAVE_FORMATS

llm_tags = ['opt_test', 'gpt_test', 't5llm_test','llama_test2','llama_test3']
label_name = "Testing"

# Create a list to store dataframes for comparison
dfs = []
labels = []

for llm_tag in llm_tags:
    # Paths
    log_dir = os.path.join(DATA_FOLDER, llm_tag)
    print(log_dir, label_name)
    
    # Load and process data
    log_files = load_log_files(log_dir, label_name)
    df = parse_logs(log_dir, log_files, label_name)
    
    # Append the dataframe and label
    dfs.append(df)
    labels.append(llm_tag)

# Ensure the save folder exists
os.makedirs(GRAPH_SAVE_FOLDER, exist_ok=True)

# Save folder for comparison plots
comparison_folder = os.path.join(GRAPH_SAVE_FOLDER, label_name+"comparison")
os.makedirs(comparison_folder, exist_ok=True)

# Plot Mean Loss comparison
plot_comparison(
    dfs, 'Epoch', 'Mean Loss', labels,
    'Mean Loss Comparison over Epochs', 'Epoch', 'Mean Loss',
    "Mean_Loss_Comparison", comparison_folder
)

# Plot Mean Accuracy comparison
plot_comparison(
    dfs, 'Epoch', 'Mean Accuracy', labels,
    'Mean Accuracy Comparison over Epochs', 'Epoch', 'Mean Accuracy',
    "Mean_Accuracy_Comparison", comparison_folder
)




import os
from utils.data_loader import load_log_files, parse_logs
from utils.plotter import plot_metric
from config.settings import GRAPH_SAVE_FOLDER, DATA_FOLDER, SAVE_FORMATS


llm_tags = ['opt_train', 'gpt_train', 't5llm_train', 'llama_train1','llama_train2','llama_train3']
label_name = "Training"

llm_tags = ['opt_test', 'gpt_test', 't5llm_test','llama_test2','llama_test3']
label_name = "Testing"

for llm_tag in llm_tags:
    
    # Paths"
    log_dir = os.path.join(DATA_FOLDER, llm_tag)
    print(log_dir,label_name)

    # Ensure the save folders exist
    os.makedirs(GRAPH_SAVE_FOLDER, exist_ok=True)

    # Add a tag to the folder for better organization
    graphs_save_folder = os.path.join(GRAPH_SAVE_FOLDER, llm_tag)

    # Ensure the tagged folder exists
    os.makedirs(graphs_save_folder, exist_ok=True)


    # Load and process data
    log_files = load_log_files(log_dir,label_name)
    df = parse_logs(log_dir, log_files,label_name)


    # Plot Mean and Median Loss over Epochs
    plot_metric(
        df, 'Epoch', ['Mean Loss', 'Median Loss'],
        [label_name + 'Mean Loss', label_name + 'Median Loss'],
        'Mean and Median Loss over Epochs', 'Epoch', 'Loss',
        label_name + "Mean_Median_Loss_Graph", graphs_save_folder
    )

    # Plot Mean Accuracy over Epochs
    plot_metric(
        df, 'Epoch', ['Mean Accuracy'],
        [label_name + 'Mean Accuracy'],
        'Mean Accuracy over Epochs', 'Epoch', 'Accuracy',
        label_name + "Mean_Accuracy_Graph", graphs_save_folder
    )

    # Plot Mean CPU Usage over Epochs
    plot_metric(
        df, 'Epoch', ['Mean CPU Usage'],
        [label_name + 'Mean CPU Usage'],
        'Mean CPU Usage over Epochs', 'Epoch', 'CPU Usage (%)',
        label_name + "Mean_CPU_Usage_Graph", graphs_save_folder
    )

    # Plot Mean RAM Usage over Epochs
    plot_metric(
        df, 'Epoch', ['Mean RAM Usage'],
        [label_name + 'Mean RAM Usage'],
        'Mean RAM Usage over Epochs', 'Epoch', 'RAM Usage (%)',
        label_name + "Mean_RAM_Usage_Graph", graphs_save_folder
    )

    # Plot Mean GPU Usage over Epochs
    plot_metric(
        df, 'Epoch', ['Mean GPU Usage'],
        [label_name + 'Mean GPU Usage'],
        'Mean GPU Usage over Epochs', 'Epoch', 'GPU Usage (%)',
        label_name + "Mean_GPU_Usage_Graph", graphs_save_folder
    )

    # Plot Mean Disk Read and Write Speed over Epochs
    plot_metric(
        df, 'Epoch', ['Mean Disk Read Speed', 'Mean Disk Write Speed'],
        [label_name + 'Mean Disk Read Speed', label_name + 'Mean Disk Write Speed'],
        'Mean Disk Read and Write Speed over Epochs', 'Epoch', 'Speed (MB/s)',
        label_name + "Mean_Disk_Speed_Graph", graphs_save_folder
    )


    # Repeat for other metrics...
