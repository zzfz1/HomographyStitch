import cv2
import matplotlib.pyplot as plt
import sticher
# import helper as hlp

if __name__ == '__main__':

    # load the source images in data folder
    imgs = [cv2.imread('data/1.jpg'),
            cv2.imread('data/2.jpg'),
            cv2.imread('data/3.jpg'),
            cv2.imread('data/4.jpg'),
            cv2.imread('data/5.jpg')]
    # imgs = [cv2.imread('data/GroupRoom/1.jpg'),
    #         cv2.imread('data/GroupRoom/2.jpg'),
    #         cv2.imread('data/GroupRoom/3.jpg'),
    #         cv2.imread('data/GroupRoom/4.jpg'),
    #         cv2.imread('data/GroupRoom/5.jpg')]

    # Show the images in the same figure

    plt.figure(figsize=(20, 10))
    output = sticher.stitch_all(imgs,method='SIFT',crop=True)
    plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))

    plt.show()
