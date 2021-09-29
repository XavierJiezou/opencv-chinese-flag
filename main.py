import cv2
import sys
from tqdm import tqdm
import numpy as np
import concurrent.futures as cf


def main(im_1_path: str, im_2_path: str = 'flag.png'):
    """Add a Chinese flag to your avatar

    Args:
        im_1_path (str): Path of your avatar image.
        im_2_path (str, optional): Path of the Chinese flag. Defaults to 'flag.png'.
    """
    im_1 = cv2.imread(im_1_path, flags=cv2.IMREAD_COLOR)
    size = [max(im_1.shape)]*2
    im_2 = cv2.imread(im_2_path, flags=cv2.IMREAD_UNCHANGED)
    im_2 = cv2.resize(im_2, size)
    alpha = np.repeat(im_2[:, :, 3]/255, 3).reshape(im_1.shape[0], im_1.shape[1], 3)
    im_3 = im_1*(1-alpha)+im_2[:, :, :3]*alpha
    cv2.imwrite('_new.jpg', im_3)


if __name__ == '__main__':
    main(sys.argv[1])