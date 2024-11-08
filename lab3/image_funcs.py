import cv2
import matplotlib.pyplot as plt
import numpy as np


def load_image(input_path: str) -> np.ndarray:
    """
    Loads the image in the specified path.

    :param input_path: Path to the input image file.
    :return: The loaded image as a NumPy array.
    """
    image = cv2.imread(input_path)
    if image is None:
        raise FileNotFoundError(f"Ошибка: не удалось загрузить изображение в: '{input_path}'.")
    return image


def display_image(title: str, image: np.ndarray) -> None:
    """
    Displays an image with a given title.

    :param title: str - Title for the display window.
    :param image: numpy.ndarray - The image to be displayed.
    :return: None
    """
    try:
        plt.figure(figsize=(8, 8))
        plt.title(title)
        plt.axis("off")
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.show()
    except Exception as e:
        raise RuntimeError(f"Не удалось вывести изображение  '{title}'") from e


def resize_image(image: np.ndarray, width: int, height: int) -> np.ndarray:
    """
    Resizes an image to the specified width and height.

    :param image: The image to resize.
    :param width: New width of the image.
    :param height: New height of the image.
    :return: The resized image.
    """
    try:
        resized_image = cv2.resize(image, (width, height))
        return resized_image
    except Exception as e:
        raise ValueError(f"Не удалось поменять разрешение изображение на {width}x{height}") from e


def save_image(output_path: str, image: np.ndarray) -> None:
    """
    Saves the image to the specified output path.

    :param output_path: Path to save the output image.
    :param image: The image to save.
    """
    success = cv2.imwrite(output_path, image)
    if not success:
        raise IOError(f"Не удалось сохранить изображение в '{output_path}'.")
