import argparse


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments.
    :return: Namespace with parsed arguments
    """
    parser = argparse.ArgumentParser(description="Process images and create annotations.")
    parser.add_argument('path_to_images', type=str, help='Path to the directory with images')
    parser.add_argument('path_to_csv', type=str, help='Path to the output CSV file')
    parser.add_argument('max_height', type=int, help='Maximum allowed image height')
    parser.add_argument('max_width', type=int, help='Maximum allowed image width')
    return parser.parse_args()