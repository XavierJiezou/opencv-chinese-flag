import cv2
import sys
from tqdm import tqdm
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
    im_3 = im_1
    for i in tqdm(range(im_1.shape[0])):
        for j in range(im_1.shape[1]):
            alpha = im_2[i, j, 3]/255
            im_3[i, j] = im_1[i, j]*(1-alpha)+im_2[i, j, :3]*alpha
    cv2.imwrite('_new.jpg', im_3)


if __name__ == '__main__':
    main(sys.argv[1])
