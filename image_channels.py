import cv2
import numpy as np

# read the image
for i in range(1,12):
    path = "banana_data/banana/banana (" + str(i) + ").jpg"
    img = cv2.imread(path)

    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb_image = (rgb_image*255).astype(np.uint8)
    cv2.imwrite(path, rgb_image)
    # find the number of channels
    channels = img.shape[2]

    print("Number of channels:", channels)
    
    