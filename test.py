try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output
import cv2

#print(pytesseract.image_to_data(Image.open('test.png')))
#quit()
#img = cv2.imread('image.jpg')
img = cv2.imread('image.png')
#print(img)


d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d)
#quit()
n_boxes = len(d['level'])
print(n_boxes)
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
