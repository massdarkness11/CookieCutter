
import cv2
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')
file_name = "turtle_for_becca.png"
file_name_export = file_name[0:-4] + "_final.png"

img = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)
bgr = img[:,:,:3] # Channels 0..2
*_, alpha = cv2.split(img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.figure(figsize=(8,8))
#plt.imshow(img)
#plt.axis("off")
#plt.title("Original Image")
#plt.show()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.figure(figsize=(8,8))
#plt.imshow(img_gray,cmap="gray")
#plt.axis("off")
#plt.title("GrayScale Image")
#plt.show()

img_invert = cv2.bitwise_not(img_gray)
#plt.figure(figsize=(8,8))
#plt.imshow(img_invert,cmap="gray")
#plt.axis("off")
#plt.title("Inverted Image")
#plt.show()

img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
#plt.figure(figsize=(8,8))
#plt.imshow(img_smoothing,cmap="gray")
#plt.axis("off")
#plt.title("Smoothen Image")
#plt.show()

final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
#plt.figure(figsize=(8,8))
#plt.imshow(final,cmap="gray")
#plt.axis("off")
#plt.title("final Image")
#plt.show()

brg = cv2.cvtColor(final,cv2.COLOR_BGR2RGB)
result = np.dstack([brg, alpha]) 
#plt.figure(figsize=(8,8))
#plt.imshow(result,cmap="gray")
#plt.axis("off")
#plt.title("clear background Image")
#plt.show()

#for x in range(int(255/5)):

#    (thresh, blackAndWhiteImage) = cv2.threshold(result, x*5, 255, cv2.THRESH_BINARY)
#    plt.figure(figsize=(8,8))
#    plt.imshow(blackAndWhiteImage,cmap="gray")
#    plt.axis("off")
#    plt.title(str(x*5) +" threshold background Image")
#    plt.show()
(thresh, blackAndWhiteImage) = cv2.threshold(result, 50, 255, cv2.THRESH_BINARY)
plt.figure(figsize=(8,8))
plt.imshow(blackAndWhiteImage,cmap="gray")
plt.axis("off")
plt.title("50 threshold background Image")
plt.show()


plt.figure(figsize=(20,20))
plt.subplot(1,6,1)
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.subplot(1,6,2)
plt.imshow(img_gray,cmap="gray")
plt.axis("off")
plt.title("GrayScale Image")
plt.subplot(1,6,3)
plt.imshow(img_invert,cmap="gray")
plt.axis("off")
plt.title("Inverted Image")
plt.subplot(1,6,4)
plt.imshow(img_smoothing,cmap="gray")
plt.axis("off")
plt.title("Smoothen Image")
plt.subplot(1,6,5)
plt.imshow(final,cmap="gray")
plt.axis("off")
plt.title("Final Sketch Image")
plt.subplot(1,6,6)
plt.imshow(result,cmap="gray")
plt.axis("off")
plt.title("Export Sketch Image")

plt.show()
cv2.imwrite(file_name_export, final)