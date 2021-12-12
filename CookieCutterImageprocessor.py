
import cv2
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')
default_area = 225625 #475 by 475
def resize(img, default_area, scale = 100):
    height, width, channels = img.shape
    if scale != 100:
        scale_percent = scale # percent of original size
    else:
        scale_percent = default_area/(height*width)* 100
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
  
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

def show(img, title):
    plt.figure(figsize=(8,8))
    plt.imshow(img,cmap="gray")
    plt.axis("off")
    plt.title(title)
    plt.show()

def fill(img):
    show(img, "original")
    th, im_th = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV);

# Copy the thresholded image.
    im_floodfill = im_th.copy()
    show(im_floodfill, "threshold image")
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    show(mask, "mask")

# Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0,0), 255);
    show(im_floodfill, "floodfill")
# Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    show(im_floodfill_inv, "floodfill inverse")

# Combine the two images to get the foreground.
    im_out = im_th | im_floodfill_inv
    return im_out


file_name = "Bulbasaur.png"
file_name_export = file_name[0:-4] + "_final.png"

img = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)
img = resize(img, default_area)




bgr = img[:,:,:3] # Channels 0..2
*_, alpha = cv2.split(img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
show(img, "original image")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show(img_gray, "gray image")

img_invert = cv2.bitwise_not(img_gray)
show(img_invert, "Inverted Image")


img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
show(img_smoothing,"Smoothen Image")


final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
show(final,"final Image")
#filled = fill(final)
#show(filled, "filled")

brg = cv2.cvtColor(final,cv2.COLOR_BGR2RGB)
result = np.dstack([brg, alpha]) 
show(result,"clear background Image")



plt.figure(figsize=(200,200))
#plt.subplots(7,8,False, True)
for x in range(int(255/5)):

    (thresh, blackAndWhiteImage) = cv2.threshold(result, x*5, 255, cv2.THRESH_BINARY)
    
    plt.subplot(7,8,x + 1)
    plt.imshow(blackAndWhiteImage,cmap="gray")
    plt.axis("off")
    plt.title(str(x*5))

plt.show()

threshold = int(input("Desired Threshold between 0 and 225"))
(thresh, blackAndWhiteImage) = cv2.threshold(result, threshold, 255, cv2.THRESH_BINARY)
show(blackAndWhiteImage, str(threshold) + " threshold background Image")

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# draw contours on the original image

image_copy = blackAndWhiteImage.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

# see the results
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)



#plt.figure(figsize=(20,20))
#plt.subplot(1,6,1)
#plt.imshow(img)
#plt.axis("off")
#plt.title("Original Image")
#plt.subplot(1,6,2)
#plt.imshow(img_gray,cmap="gray")
#plt.axis("off")
#plt.title("GrayScale Image")
#plt.subplot(1,6,3)
#plt.imshow(img_invert,cmap="gray")
#plt.axis("off")
#plt.title("Inverted Image")
#plt.subplot(1,6,4)
#plt.imshow(img_smoothing,cmap="gray")
#plt.axis("off")
#plt.title("Smoothen Image")
#plt.subplot(1,6,5)
#plt.imshow(final,cmap="gray")
#plt.axis("off")
#plt.title("Final Sketch Image")
#plt.subplot(1,6,6)
#plt.imshow(result,cmap="gray")
#plt.axis("off")
#plt.title("Export Sketch Image")

#plt.show()
#cv2.imwrite(file_name_export, blackAndWhiteImage)
