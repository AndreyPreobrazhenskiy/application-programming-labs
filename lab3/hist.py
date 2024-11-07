import cv2
import numpy as np
import matplotlib.pyplot as plt


def make_hist(image):
    """
    Generates and displays the histogram for each color channel in the image.

    :param image: The image for which the histogram is calculated.
    """
    colors = ('b', 'g', 'r')
    plt.figure(figsize=(10, 5))
    plt.title("Гистограмма цветовых каналов")
    plt.xlabel("Интенсивность")
    plt.ylabel("Частота")

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)
        plt.xlim([0, 256])
    plt.show()