from annotation import annotation
from annotation import dataframe
from image_funcs import add_area
from image_funcs import add_image_info
from image_funcs import filter_df
from hist import hist
from parser import parse_arguments


def main():
    try:
        args = parse_arguments()
        annotation(args.path_to_csv, args.path_to_images)
        df = dataframe(args.path_to_csv)
        df = add_image_info(df)
        print("\nStatistical Summary:")
        print(df[['Height', 'Width', 'Channels']].describe())
        filtered_df = filter_df(df, args.max_height, args.max_width)
        filtered_df = add_area(filtered_df)
        sorted_df = filtered_df.sort_values(by='Area', ascending=True)
        hist(sorted_df)

        print("\nProcessing complete. Results:")
        print(sorted_df)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
