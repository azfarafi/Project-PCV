import cv2
import numpy as np

img = cv2.imread('test_image_lena_noisy.png')
img2 = cv2.imread('test_image_lena_ori.png')


#MEDIAN
baris, kolom, ch = img.shape 
img_median = np.zeros_like(img)

for k in range(ch):
    layer = img[:,:,k]
    padded = np.pad(layer, pad_width = 2, mode = 'reflect')

    for i in range(baris):
        for j in range(kolom):
            jendela = padded [i:i+5, j:j+5]
            img_median[i, j, k] = np.median(jendela)

#HISTOGRAM
hist = np.bincount(img.ravel(), minlength=256)
cdf = np.cumsum(hist)
cdf_normalized = cdf * 255 / cdf[-1]
lut = np.round(cdf_normalized).astype(np.uint8)
img_histogram = lut[img_median]

#SHARPENING
kernel_sharpen = np.array([ [0, -1, 0],
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




#cv2.imshow ('Lena Noisy', img)
cv2.imshow ('Lena Original', img2)
cv2.imshow('Lena Gabungan Median, Histogram, dan Sharpening', img_sharpen)

cv2.waitKey(0)