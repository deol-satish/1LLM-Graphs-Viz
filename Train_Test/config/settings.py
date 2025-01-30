# Configuration variables
GRAPH_SAVE_FOLDER = "output/graphs/"
DATA_FOLDER = "data"
LOG_FILE_ORIGINAL = "./data/eval_logs_original.json"
LOG_FILE_LLM = "./data/eval_logs_llm.json"
SAVE_FORMATS = ['png', 'eps', 'pdf']  # Formats to save graphs
DPI = 500

# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#ff6347']  # Add more colors as needed
# markers = ['o', 's', 'D', '^', 'v', 'p', '*', 'x']       # Add more markers as needed
# linestyles = ['-', '--', '-.', ':']                      # Add more linestyles as needed

colors = ['orange', 'blue', 'c', 'g', 'm', 'y', 'k', '#ff6347']  # Add more colors as needed
markers = ['', '', '', '^', 'v', 'p', '*', 'x']       # Add more markers as needed
linestyles = ['-', '-', '-.', ':']                      # Add more linestyles as needed

COL_DICT = {
    'queue_type': 0,
    'burst_allowance': 1,
    'drop_probability': 2,
    'current_queue_delay': 3,
    'accumulated_probability': 4,
    'average_dequeue_time': 5,
    'length_in_bytes': 6,
    'total_drops': 7,
    'packet_length': 8
}


bar_width = 0.3

figsize = (8,6)

title_req = True
