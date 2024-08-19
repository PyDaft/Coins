import numpy as np
import cv2
import os

os.chdir('C:\\Users\\abhin\\Documents\\Python_Resources\\Python Scripts\\capstone\\') #changes to the directory where my file stored.THis step is required if you have a difernt directory than the place VS code is installed
# function to fetch radius
def get_radius(circles):
    radius = []
    for coords in circles[0,:]:
        radius.append(coords[2])
    return radius

def av_pix(img,circles,size):
    av_value =[]
    for coords in circles[0,:]:
        col =np.mean(img[coords[1]-size:coords[1]+size,coords[0]-size:coords[0]+size])
        # print(img[coords[1]-size,coords[1]+size,coords[0]-size,coords[0]+size])
        av_value.append(col)

    return av_value

# reading the image using open CV 
# you can read the documentation here - 
img = cv2.imread('capstone_coins.png',cv2.IMREAD_GRAYSCALE) #reading the document and making it grayscale as we dont want to use color attribute and use grayscale image to work on
original_image = cv2.imread('capstone_coins.png')
img = cv2.GaussianBlur(img, (5,5), 0)



# Using Hough Circle Transform 

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,0.9,120,param1=50, param2=27,minRadius=60, maxRadius=120)
print(circles) #cooridnates of the circle followed by the radius
circles = np.uint16(np.around(circles))


count = 1
for i in circles[0,:]:
    # draw the outer circle
    # cooridnate and radius along wwith RGB format and thikcness
    cv2.circle(original_image,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center circle
    cv2.circle(original_image,(i[0],i[1]),2,(0,255,0),3)
    # cv2.putText(original_image,str(count),(i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
    count += 1

# classify the coins basis the radius and the brightness so that we can then move to adding them all together
# 
#A: Value fpr the radius 

radii = get_radius(circles)
print(radii)

# B:get brightness values
bright_values = av_pix(img,circles,20) 
print(bright_values)


# now all we need to do here is to classify the value of the coin using if and else statement
values = []
for a,b in zip(bright_values, radii):
    if a>150 and b >110:
        values.append(10)
    if a>150 and b <=110:
        values.append(5)
    if a<150 and b>110:
        values.append(2)
    if a<150 and b<110:
        values.append(1)

print(values)
print(sum(values))

# Label the images with the pence and show case on the image

count_2 = 0
for i in circles[0,:]:
    cv2.putText(original_image,str(values[count_2])+'p',(i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
    count_2 +=1
cv2.putText(original_image,'ESTIMATED TOTAL VALUE OF THE COINS: '+str(sum(values)),(200,100), cv2.FONT_HERSHEY_SIMPLEX,1.4,255)
        




cv2.imshow('Detected Coins', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



