from os import listdir, makedirs
from pathlib import Path
from PIL import Image
import math

import multiprocessing as mp
import time

EPS_DIR = 'eps_images'
JPGS_DIR = 'jpg_images'
EXPECTED_FILE_NAMES = ['flowers', 'pengu', 'stripes']

JPG_SUFFIX = '.jpg'
EPS_SUFFIX = '.eps'

MAX_DIM = 1920

def convert_image(eps_image: Path, jpg_image_dir: Path):
    def resize_image(img: Image, max_dim: int = MAX_DIM):
        w, h = img.size
        scale = max_dim / max(w, h)
        new_w, new_h = int(w * scale), int(h * scale)
        return img.resize((new_w, new_h), resample=Image.LANCZOS)

    try:
        image = Image.open(eps_image)
        scale = math.sqrt(89478485/(image.width*image.height))
        image = resize_image(image, max_dim=MAX_DIM)
        image.save(jpg_image_dir / (eps_image.stem + JPG_SUFFIX))

        return f'Successfully converted {eps_image.name}'
    except:
        return f'ERROR: Failed to convert {eps_image.name}'
    
def validate_env(eps_image_dir: Path):
    if (not eps_image_dir.exists()):
        raise('eps or jpg dir does not exist')
    for expected_file in EXPECTED_FILE_NAMES:
        expected_file_path = eps_image_dir / (expected_file + EPS_SUFFIX)
        if (not expected_file_path.exists()):
            raise(f'{expected_file_path} does not exist')

def setup_env(jpg_image_dir: Path):
    if (not jpg_image_dir.exists()):
        makedirs(jpg_image_dir)

def main():

    parent_dir = Path(__file__).parent.resolve()
    eps_image_dir = parent_dir / EPS_DIR
    eps_images = [eps_image_dir / file for file in listdir(eps_image_dir)]
    jpg_image_dir = parent_dir / JPGS_DIR

    validate_env(eps_image_dir)

    setup_env(jpg_image_dir)

    #------------------------------------------- REPLACE THIS CODE -------------------------------------------

    # convert images one-by-one, then print results (in case of error)
    for eps_image in eps_images:
        res = convert_image(eps_image, jpg_image_dir)
        print(res)

    # Tasks:
    #   1. Parallelize the tasks so that multiple files can be converted at once
    #   2. Log the time it takes for these tasks to run (in seconds).

    #---------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()