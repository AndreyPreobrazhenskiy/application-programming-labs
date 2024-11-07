import cv2
import matplotlib.pyplot as plt


def load_image(input_path):
    """
    Loads the image in the specified path.

    :param input_path: Path to the input image file.
    :return: The loaded image as a NumPy array.
    """
    image = cv2.imread(input_path)
    if image is None:
        raise FileNotFoundError(f"Ошибка: не удалось загрузить изображение по пути '{input_path}'.")
    print("Размер исходного изображения:", image.shape)
    return image


def display_image(title, image):
    """
    Displays an image with a given title.

    :param title: str - Title for the display window.
    :param image: numpy.ndarray - The image to be displayed.
    :return: None
    """
    plt.figure(figsize=(8, 8))
    plt.title(title)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()


def resize_image(image, width, height):
    """
    Resizes an image to the specified width and height.

    :param image: The image to resize.
    :param width: New width of the image.
    :param height: New height of the image.
    :return: The resized image.
    """
    return cv2.resize(image, (width, height))


def save_image(output_path, image):
    """
    Saves the image to the specified output path.

    :param output_path: Path to save the output image.
    :param image: The image to save.
    """
    cv2.imwrite(output_path, image)