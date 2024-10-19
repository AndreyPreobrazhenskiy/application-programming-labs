import csv
import os

def annotation(imgdir: str, output_csv: str) -> None:
    """
    Creates annotation with absolute and relative paths to downloaded images
    :param imgdir: directory with saved images
    :param output_csv: csv file that will be used to write annotation
    """
    img_filenames = collect_filenames(imgdir)
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['absolute_path', 'relative_path']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for filename in img_filenames:
            relative_path = os.path.relpath(filename, start=imgdir)
            absolute_path = os.path.abspath(filename)
            writer.writerow({'absolute_path': absolute_path, 'relative_path': relative_path})


def collect_filenames(imgdir: str) -> list:
    """
    Collect filenames of downloaded images.
    :param imgdir: directory with saved images
    :return: list of filenames in this directory
    """
    img_extensions = ('.png', '.jpg', '.jpeg')
    img_filenames = []
    for filename in os.listdir(imgdir):
        if filename.lower().endswith(img_extensions):
            img_filenames.append(filename)
    return img_filenames