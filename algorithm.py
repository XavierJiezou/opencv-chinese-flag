import cv2
import sys
import numpy as np


def algorithm(im_1_path: str, im_2_path: str = 'img/flag.png', im_3_path: str = 'img/_new.jpg'):
    """Add a Chinese flag to your avatar

    Args:
        im_1_path (str): Path of your avatar image.
        im_2_path (str, optional): Path of the Chinese flag. Defaults to 'flag.png'.
        im_3_path (str): Path to save the composite image. Defaults ot `_new.jpg`.
    """
    im_1 = cv2.imread(im_1_path, flags=cv2.IMREAD_COLOR)
    h, w, _ = im_1.shape
    im_2 = cv2.imread(im_2_path, flags=cv2.IMREAD_UNCHANGED)
    im_2 = cv2.resize(im_2, [max(h, w)]*2)[0:h, 0:w, :]
    alpha = np.expand_dims(im_2[:, :, 3]/255, 2).repeat(3, axis=2)
    im_3 = im_1*(1-alpha)+im_2[:, :, :3]*alpha
    cv2.imwrite(im_3_path, im_3)


if __name__ == '__main__':
    algorithm(sys.argv[1])
