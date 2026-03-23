# Updated veri_gorsellestir.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# assuming 'data' is your dataset

def save_visualization(data, filename):
    plt.figure(figsize=(10, 6))  # Improved layout
    
    # Example visualization (modify according to your data)
    plt.plot(data['x'], data['y'], label='Data visualization')
    plt.title('Visualization Title')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.legend()
    plt.grid()  
    plt.savefig(filename + '.png', format='png')  # Save as PNG
    plt.close()


def statistical_summary(data):
    summary = data.describe()  # Generate statistical summary
    print(summary)
    return summary


# Example usage:
data = pd.DataFrame({'x': np.arange(10), 'y': np.random.rand(10)})
save_visualization(data, 'visualization_output')
statistical_summary(data)