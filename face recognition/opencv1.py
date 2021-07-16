# Importing required libraries
import cv2

# Loading the trained XML classifier 
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Loading captured images
imp_img = cv2.VideoCapture('elon.jpg')

# Reading captured image
res, img = imp_img.read() # declared two variable as .read() outputs 2 values
                          # 1. result: whether the image is present or not with true/false
                          # 2. resolution: outputs resolution of the image

# Converting image to grayscale as our xml file is specialised for grayscale images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # take inputs : 1.image
                                             #               2. color type

# Detect faces of different sizes in the input image
faces = detect.detectMultiScale(gray, 1.3, 5) # takes inputs: 1. image
                                              #               2. scale factor
                                              #               3. minNeighbor

# Drawing rectangle/ square over the image
# for loop takes all the outputs from the faces which are cordinates x and y of the first point
# and w: width and h: height of the face
for x, y, w, h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 0), 2)
    # attributes of cv2.rectangle are 
    # 1. image
    # 2. first cordinates (bottom left)
    # 3. cordinates of top right corner
    # 4. color or rectangle
    # 5. thickness of rectangle

# Show/Print image 
cv2.imshow("Elon Image", img) # attributes are: 1. title; 2. image

cv2.waitKey(0) #Sets the time for which the image will be shown. 0 will take it as manual
imp_img.release() # releasing the image to be shown
cv2.destroyAllWindows() # Destory or free all the resources after the image is shown

