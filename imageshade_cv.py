import cv2

image = cv2. imread ("open_cv/image/pikachu.jpeg", 1)
# Split the above image in red, blue and green different saturations 
B, G, R = cv2.split(image)

cv2.imshow("original", image)
cv2.waitKey(5000)

cv2.imshow("Blue Saturation Image", B)
cv2.waitKey(5000)

cv2.imshow("Green Saturation Image", G)
cv2.waitKey(5000)

cv2. imshow("Red Saturation Image", R)
cv2.waitKey(5000)

cv2.destroyAllWindows()