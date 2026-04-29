import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('input/lena_noisy.png')

# MEDIAN
baris, kolom, ch = img.shape 
img_median = np.zeros_like(img)

for k in range(ch):
    layer = img[:,:,k]
    padded = np.pad(layer, pad_width=2, mode='reflect')

    for i in range(baris):
        for j in range(kolom):
            jendela = padded[i:i+5, j:j+5]
            img_median[i, j, k] = np.median(jendela)

# HISTOGRAM
hist = np.bincount(img.ravel(), minlength=256)
cdf = np.cumsum(hist)
cdf_normalized = cdf * 255 / cdf[-1]
lut = np.round(cdf_normalized).astype(np.uint8)
img_histogram = lut[img_median]

# SHARPENING
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]], np.float32)

img_sharpen = np.zeros_like(img_histogram)
for k in range(ch):
    layer_hist = img_histogram[:,:,k]
    padded = np.pad(layer_hist, pad_width=1, mode='reflect')
        
    for i in range(baris):
        for j in range(kolom):
            jendela = padded[i:i+3, j:j+3]
            nilai = (jendela * kernel_sharpen).sum()
            img_sharpen[i, j, k] = np.clip(nilai, 0, 255)



plt.figure(figsize=(12,10))


plt.subplot(5,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Image Noisy")
plt.axis('off')

plt.subplot(5,2,2)
plt.hist(img.ravel(), bins=256)
plt.title("Histogram Noisy")


plt.subplot(5,2,3)
plt.imshow(cv2.cvtColor(img_median, cv2.COLOR_BGR2RGB))
plt.title("Median Filter (Denoised)")
plt.axis('off')

plt.subplot(5,2,4)
plt.hist(img_median.ravel(), bins=256)
plt.title("Histogram Median")


plt.subplot(5,2,5)
plt.imshow(cv2.cvtColor(img_histogram, cv2.COLOR_BGR2RGB))
plt.title("Histogram Equalization")
plt.axis('off')

plt.subplot(5,2,6)
plt.hist(img_histogram.ravel(), bins=256)
plt.title("Histogram Equalized")


plt.subplot(5,2,7)
plt.imshow(cv2.cvtColor(img_sharpen, cv2.COLOR_BGR2RGB))
plt.title("Sharpened")
plt.axis('off')

plt.subplot(5,2,8)
plt.hist(img_sharpen.ravel(), bins=256)
plt.title("Histogram Sharpened")


plt.subplot(5,2,9)
plt.imshow(cv2.cvtColor(img_sharpen, cv2.COLOR_BGR2RGB))
plt.title("Final Image")
plt.axis('off')

plt.subplot(5,2,10)
plt.hist(img_sharpen.ravel(), bins=256)
plt.title("Final Histogram")

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
