
import os
from config.settings import GRAPH_SAVE_FOLDER, DATA_SAVE_FOLDER, LOG_FILE_ORIGINAL, LOG_FILE_LLM, SAVE_FORMATS, DPI
from utils.dataframe_utils import create_dataframe,load_logs, extract_data, return_extract_data
from utils.plotter import plot_line_comparison, plot_box_comparison, cdf_plot_line_comparison
eval_tag = "llama_eval"
# Ensure the save folders exist
os.makedirs(GRAPH_SAVE_FOLDER, exist_ok=True)
os.makedirs(DATA_SAVE_FOLDER, exist_ok=True)

# Load and extract data
original_logs = load_logs(LOG_FILE_ORIGINAL)
llm_logs = load_logs(LOG_FILE_LLM)
steps_original, queue_delays_original, packet_lengths_original, losses_original = extract_data(original_logs)
steps_llm, queue_delays_llm, packet_lengths_llm, losses_llm = extract_data(llm_logs)

# Create DataFrame
df, cdf_df = create_dataframe(steps_original, queue_delays_original, packet_lengths_original, losses_original,
                        steps_llm, queue_delays_llm, packet_lengths_llm, losses_llm)

cdf_df.to_csv(f"{DATA_SAVE_FOLDER}/CDFprocessed_data.csv", index=True)


# Save processed DataFrame (optional)
df.to_csv(f"{DATA_SAVE_FOLDER}/processed_data.csv", index=True)

# Add a tag to the folder for better organization
tagged_folder = os.path.join(GRAPH_SAVE_FOLDER, eval_tag)

# Ensure the tagged folder exists
os.makedirs(tagged_folder, exist_ok=True)




# Plot queue delay comparison using the updated line plot function
plot_line_comparison(
    df,
    columns=['Original Queue Delay', 'LLM Queue Delay'],
    labels=['Traditional L4S', 'L4S-LLM'],
    xlabel='Step Number',
    ylabel='Queue Delay (s)',
    title='Queue Delay Comparison: Traditional vs LLAMA',
    filename=f"{eval_tag}_queue_delay_comparison",
    folder=tagged_folder
)

# Plot queue delay box plot comparison using the updated box plot function
plot_box_comparison(
    df,
    columns=['Original Queue Delay', 'LLM Queue Delay'],
    labels=['Traditional L4S', 'L4S-LLM AQM'],
    ylabel='Queue Delay (s)',
    title='Queue Delay Comparison (Box Plot): Traditional vs LLAMA',
    filename=f"{eval_tag}_queue_delay_box_comparison",
    folder=tagged_folder
)

# Plot throughput comparison using the updated line plot function
plot_line_comparison(
    df,
    columns=['Original Throughput', 'LLM Throughput'],
    labels=['Traditional L4S', 'L4S-LLM AQM'],
    xlabel='Step Number',
    ylabel='Bandwidth Utilisation (Mbit/s)',
    title='Throughput Comparison: Traditional vs LLAMA',
    filename=f"{eval_tag}_throughput_comparison",
    folder=tagged_folder
)

# Plot throughput box plot comparison using the updated box plot function
plot_box_comparison(
    df,
    columns=['Original Throughput', 'LLM Throughput'],
    labels=['Traditional L4S', 'L4S-LLM AQM'],
    ylabel='Bandwidth Utilisation (Mbit/s)',
    title='Bandwidth Utilisation Comparison (Box Plot): Traditional vs LLAMA',
    filename=f"{eval_tag}_throughput_box_comparison",
    folder=tagged_folder
)



# Plot throughput CDF comparison
cdf_plot_line_comparison(
    cdf_df,
    index_rows='Original Throughput Sorted',
    columns=['Original Throughput CDF', 'LLM Throughput CDF'],
    labels=['Traditional L4S', 'L4S-LLM AQM'],
    xlabel='Bandwidth Utilisation (Mbps)',
    ylabel='CDF',
    title='Bandwidth Utilisation CDF Comparison',
    filename=f"{eval_tag}_throughput_cdf_comparison",
    folder=tagged_folder
)

# Plot queue delay CDF comparison
cdf_plot_line_comparison(
    cdf_df,
    index_rows='Original Queue Delay Sorted',
    columns=['Original Queue Delay CDF', 'LLM Queue Delay CDF'],
    labels=['Traditional L4S', 'L4S-LLM AQM'],
    xlabel='Queue Delay (s)',
    ylabel='CDF',
    title='Queue Delay CDF Comparison',
    filename=f"{eval_tag}_queue_delay_cdf_comparison",
    folder=tagged_folder
)


eval_tag = "llama_eval"
# Ensure the save folders exist
os.makedirs(GRAPH_SAVE_FOLDER, exist_ok=True)
os.makedirs(DATA_SAVE_FOLDER, exist_ok=True)

# Load and extract data
original_logs = load_logs(LOG_FILE_ORIGINAL)
llm_logs = load_logs(LOG_FILE_LLM)
steps_original, queue_delays_original, packet_lengths_original, losses_original, returns_original = return_extract_data(original_logs)
steps_llm, queue_delays_llm, packet_lengths_llm, losses_llm, returns_llm = return_extract_data(llm_logs)

import pandas as pd

dict = {
    "oreturns":returns_original,
    "lreturns":returns_llm
}
return_df = pd.DataFrame(dict)


plot_line_comparison(
    return_df,
    columns=['oreturns', 'lreturns'],
    labels=['Original return', 'LLM return'],
    xlabel='Step Number',
    ylabel='return',
    title='return Comparison: Original vs LLAMA',
    filename="sample_test_seq_return_comparison",
    folder="sample_test_seq"
)



