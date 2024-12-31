import cv2
# Read
image = cv2.imread("image.jpg")

# Show
cv2.imshow("Image", image)

# Write
cv2.imwrite("output.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
