from hist import make_hist
from image_funcs import display_image
from image_funcs import load_image
from image_funcs import resize_image
from image_funcs import save_image
from parser import parse_arguments


def main():
    args = parse_arguments()
    image = load_image(args.input_path)
    make_hist(image)
    display_image("Исходное изображение", image)
    resized_image = resize_image(image, args.width, args.height)
    display_image("Измененное изображение", resized_image)
    save_image(args.output_path, resized_image)


if __name__ == "__main__":
    main()
