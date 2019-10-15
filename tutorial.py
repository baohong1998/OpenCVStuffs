
import imutils
import cv2
print(cv2.__version__)
image = cv2.imread("./opencv-tutorial/jp.png")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# display image
cv2.imshow("Image", image)
cv2.waitKey(0)

# display ROI
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# diplay a pixel
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# reszie with respect ratio
r = 300.0/w
dim = (300, int(h*r))
resize = cv2.resize(image, dim)
cv2.imshow("resize", resize)
cv2.waitKey(0)

# imutils resizing
resize = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resize)
cv2.waitKey(0)

# imutils resizing
rotated = imutils.rotate_bound(image, -45)
cv2.imshow("Imutils rotation", rotated)
cv2.waitKey(0)

# apply a Gaussian Blur with a 11x11 kernel
# useful to reducing high freq noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# draw circle
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# draw a 5px thick red line
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# draw green text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park", (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
