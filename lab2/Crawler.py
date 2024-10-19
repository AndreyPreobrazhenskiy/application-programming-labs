import os

from icrawler.builtin import GoogleImageCrawler


def install_images(kw: str, imgdir: str, num: int)->None:
    """
    This function searches images by keyword in Google and downloads them to the directory. (Clears the directory every time the script is run).
    :param kw: keyword for searching
    :param num: how many images you want to download
    :param imgdir: directory to save images
    """
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)
    for filename in os.listdir(imgdir):
        os.remove(os.path.join(imgdir, filename))
    google_crawler = GoogleImageCrawler(downloader_threads=4, storage={'root_dir': imgdir})
    google_crawler.crawl(keyword=kw, max_num=num)