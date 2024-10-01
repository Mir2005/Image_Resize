import cv2

source = "YOUR_IMG_FILE_NAME" # enter the name of your file
destination = "NEW_FILE_NAME.EXTENSIONS" # enter a new file name with extension which you want to create
scale_percent = 50

img = cv2.imread(source, cv2.IMREAD_UNCHANGED)



new_width = int(img.shape[1] * scale_percent / 100)
new_height = int(img.shape[0] * scale_percent / 100)

output = cv2.resize(img, (new_width, new_height))

cv2.imwrite(destination, output)

cv2.waitKey(0)