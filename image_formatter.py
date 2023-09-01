import os
import glob
from PIL import Image


def main():
    options = get_options()

    input("Enter to start")
    check_dir(options['out_dir'])
    if os.path.exists(options['in_dir']):
        files = glob.glob(f"{options['in_dir']}/*")
        for i in range(len(files)):
            im = Image.open(files[i])
            im = convert(im, options['extension'])
            im.save(f"{options['out_dir']}/{options['prefix']}_{i:04}.{options['extension']}")
            print(f"\rprogress... {i+1}/{len(files)}", end='')
    else:
        print("input directory does not exist")
        return


def get_options():
    options = {}
    options['in_dir']    = "inputs/" + input("Input input directory: ")
    options['out_dir']   = "outputs/" + input("Input output directory: ")
    options['prefix']    = input("Input prefix: ")
    options['extension'] = input("Input extension (png / jpg): ")

    return options


def check_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def convert(im, mode):
    if mode == 'png':
        im = im.convert('RGBA')
    elif mode == 'jpg':
        im = im.convert('RGB')
    
    return im


if __name__ == "__main__":
    main()
    print("\n--- end ---")