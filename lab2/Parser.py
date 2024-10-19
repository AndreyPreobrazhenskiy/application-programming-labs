import argparse

def create_parser()->tuple[str, str, str, int]:
    """
    Reads arguments from the terminal
    :return: args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('kw', type=str,help="Keyword for searching")
    parser.add_argument('imgdir',type=str,help="Where to download the images")
    parser.add_argument('output_csv',type=str,help="The name of annotation file")
    parser.add_argument('num', type=int, help="Number of images that you want to download")
    args = parser.parse_args()
    return args.kw, args.imgdir, args.output_csv, args.num