from Annotation import annotation
from Crawler import install_images
from Iterator import Iterator
from Parser import create_parser


def main():
    kw, imgdir, output_csv, num = create_parser()
    try:
        install_images(kw, imgdir, num)
        annotation(imgdir, output_csv)
        my_iterator = Iterator(output_csv)
        for item in my_iterator:
            print(item)
    except Exception as e:
        print(f"Something went wrong: {e} ")


if __name__ == "__main__":
    main()