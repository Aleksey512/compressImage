import os
from PIL import Image
import re


def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def compress_img(image_name, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True):
    img = Image.open(image_name)

    if new_size_ratio < 1.0:
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.ANTIALIAS)

    elif width and height:
        img = img.resize((width, height), Image.ANTIALIAS)

    fullname, ext = os.path.splitext(image_name)

    if to_jpg:
        new_filename = f"{fullname}_compressed.jpg"
    else:
        new_filename = f"{fullname}_compressed{ext}"

    try:
        img.save(new_filename, quality=quality, optimize=True)
    except OSError:
        img = img.convert("RGB")
        img.save(new_filename, quality=quality, optimize=True)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple Python script for compressing and resizing images")
    parser.add_argument("-i", "--image", help="Target image to compress and/or resize")
    parser.add_argument("-d", "--dir", help="Target dir to compress and/or resize all images")
    parser.add_argument("-j", "--to-jpg", action="store_true", help="Whether to convert the image to the JPEG format")
    parser.add_argument("-q", "--quality", type=int,
                        help="Quality ranging from a minimum of 0 (worst) to a maximum of 95 (best). Default is 90",
                        default=90)
    parser.add_argument("-r", "--resize-ratio", type=float,
                        help="Resizing ratio from 0 to 1, setting to 0.5 will multiply width & height of the image by 0.5. Default is 1.0",
                        default=1.0)
    parser.add_argument("-w", "--width", type=int,
                        help="The new width image, make sure to set it with the `height` parameter")
    parser.add_argument("-h", "--height", type=int,
                        help="The new height for the image, make sure to set it with the `width` parameter")
    args = parser.parse_args()
    print("=" * 50)
    if args.image:
        print("[*] Image:", args.image)
    print("[*] To JPEG:", args.to_jpg)
    print("[*] Quality:", args.quality)
    print("[*] Resizing ratio:", args.resize_ratio)
    if args.width and args.height:
        print("[*] Width:", args.width)
        print("[*] Height:", args.height)
    print("=" * 50)

    if args.image:
        compress_img(args.image, args.resize_ratio, args.quality, args.width, args.height, args.to_jpg)

    # Уменьшает размер в нужной папке только у файлов JPEG
    # Если надо для всех файлов удалить <if extension==".jpg">
    elif args.dir:
        for address, dirs, files in os.walk(f"{args.dir}"):
            for name in files:
                _, extension = os.path.splitext(os.path.join(address, name))
                if extension == ".jpg" or extension == ".JPG":
                    compress_img(os.path.join(address, name), args.resize_ratio, args.quality, args.width, args.height,
                                 args.to_jpg)
