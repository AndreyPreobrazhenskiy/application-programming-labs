from hist import create_hist
from hist import display_hist
from image_funcs import display_image
from image_funcs import load_image
from image_funcs import resize_image
from image_funcs import save_image
from parser import parse_arguments


def main():
    try:
        args = parse_arguments()
        image = load_image(args.input_path)

        hist_b, hist_g, hist_r = create_hist(image)
        display_hist(hist_b, hist_g, hist_r)

        display_image("Исходное изображение", image)
        resized_image = resize_image(image, args.width, args.height)
        display_image("Измененное изображение", resized_image)

        save_image(args.output_path, resized_image)
    except (FileNotFoundError, ValueError) as e:
        print(e)


if __name__ == "__main__":
    main()
