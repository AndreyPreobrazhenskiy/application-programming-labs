import cv2
import pandas as pd


def get_image_info(path_to_image: str) -> tuple:
    """
    Get the dimensions of an image (height, width, channels).
    :param: Path to the image
    :return: Tuple of (height, width, channels)
    """
    image= cv2.imread(path_to_image)
    if image is None:
        raise FileNotFoundError(f"Image not found: {path_to_image}")
    height, width, channels = image.shape
    return height, width, channels


def add_image_info(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add height, width, channels to a DataFrame.
    :param: Source DataFrame
    :return: Updated DataFrame with added dimensions
    """
    df = df.copy()
    heights, widths, channels_list = [], [], []

    for _, row in df.iterrows():
        try:
            height, width, channels = get_image_info(row['Absolute_Path'])
            heights.append(height)
            widths.append(width)
            channels_list.append(channels)
        except Exception as e:
            print(f"Error processing {row['Absolute_Path']}: {e}")
            heights.append(None)
            widths.append(None)
            channels_list.append(None)

    df.loc[:, 'Height'] = heights
    df.loc[:, 'Width'] = widths
    df.loc[:, 'Channels'] = channels_list
    return df


def filter_df(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    """
    Filters the DataFrame by the given height and width thresholds.
    :param: Source DataFrame
    :param: Maximum height of the image
    :param: Maximum width of the image
    :return: Filtered DataFrame
    """
    return df[(df['Height'] <= max_height) & (df['Width'] <= max_width)]


def add_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate and add the area (Height * Width) of each image to the DataFrame.
    :param: Source DataFrame
    :return: Updated DataFrame
    """
    df = df.copy()
    df['Area'] = df['Height'] * df['Width']
    return df