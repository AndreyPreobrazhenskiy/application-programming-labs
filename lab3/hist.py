import cv2
import matplotlib.pyplot as plt
import numpy as np



def create_hist(image: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generates histograms for each color channel in the image.

    :param image: The image for which the histograms are calculated.
    :return: Tuple of histograms for blue, green, and red channels.
    """
    try:
        hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
        hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])
        return hist_b, hist_g, hist_r
    except Exception as e:
        print(f"Не удалось создать гистограмму: {e}")
        raise


def display_hist(hist_b: np.ndarray, hist_g: np.ndarray, hist_r: np.ndarray) -> None:
    """
    Displays the histogram for each color channel.

    :param hist_b: Histogram for the blue channel.
    :param hist_g: Histogram for the green channel.
    :param hist_r: Histogram for the red channel.
    """
    try:
        plt.figure(figsize=(10, 5))
        plt.title("Гистограмма цветовых каналов")
        plt.xlabel("Интенсивность")
        plt.ylabel("Частота")

        plt.plot(hist_b, color='b', label='Синий')
        plt.plot(hist_g, color='g', label='Зелёный')
        plt.plot(hist_r, color='r', label='Красный')
        plt.xlim([0, 256])
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Не удалось вывести гистограмму: {e}")
