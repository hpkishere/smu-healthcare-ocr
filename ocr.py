try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import numpy as np

# Read image
img_cv = cv2.imread(r'./picture.jpg') # RPI should output in ./picture.jpg

# Convert to B&W and do a binary filter
img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(img_cv,105,235,cv2.THRESH_BINARY)

# Erode to make lines thicker
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(thresh1,kernel,iterations = 1)
cv2.imwrite('./edited.jpeg', erosion)

# Use pytesseract to read
result = pytesseract.image_to_string('./edited.jpeg', lang='eng', config='--psm 6 outputbase digits')
print(result)