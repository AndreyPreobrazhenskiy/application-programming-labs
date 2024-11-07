import argparse
import os

def parse_arguments():
    """
    Parses command-line arguments for image processing parameters.

    :return: Parsed command-line arguments containing input_path, output_path, width, and height.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', type=str, help="Путь к исходному изображению.")
    parser.add_argument('output_path', type=str, help="Путь для сохранения результата.")
    parser.add_argument('width', type=int, help="Новая ширина изображения.")
    parser.add_argument('height', type=int, help="Новая высота изображения.")
    args = parser.parse_args()

    if not os.path.isfile(args.input_path):
        raise FileNotFoundError(f"Ошибка: Файл '{args.input_path}' не найден.")

    if args.width <= 0 or args.height <= 0:
        raise ValueError("Ошибка: Ширина и высота должны быть положительными целыми числами.")

    return args