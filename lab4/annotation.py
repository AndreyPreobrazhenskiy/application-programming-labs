import csv
import os
import pandas as pd

def annotation(path_to_csv: str, path_to_images: str) -> None:
    """
    Creates a CSV annotation with absolute and relative paths to images.
    :param: Path to the CSV annotation file
    :param: Path to the directory with images
    """
    if not os.path.exists(path_to_images):
        raise FileNotFoundError(f"Directory not found: {path_to_images}")

    with open(path_to_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Absolute_Path', 'Relative_Path'])

        for image in os.listdir(path_to_images):
            absolute_path = os.path.abspath(os.path.join(path_to_images, image))
            relative_path = os.path.relpath(absolute_path)
            writer.writerow([absolute_path, relative_path])


def dataframe(path_to_csv: str) -> pd.DataFrame:
    """
    Loads data from a CSV file into a Pandas DataFrame.
    :param: Path to the CSV file
    :return: Loaded DataFrame
    """
    if not os.path.exists(path_to_csv):
        raise FileNotFoundError(f"The annotation file was not found: {path_to_csv}")
    df = pd.read_csv(path_to_csv)
    df.columns = ['Absolute_Path', 'Relative_Path']
    return df