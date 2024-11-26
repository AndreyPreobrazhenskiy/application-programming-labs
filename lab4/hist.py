import matplotlib.pyplot as plt
import pandas as pd


def hist(df: pd.DataFrame) -> None:
    """
    Creates and displays a histogram of image area distribution.
    :param: DataFrame containing image data
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['Area'], bins=20, color='blue', edgecolor='black', alpha=0.7)
    plt.title('Distribution of Image Areas')
    plt.xlabel('Area (pixels)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()