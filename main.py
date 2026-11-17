#filled rectangle
import cv2

image = cv2.imread("pika.png")

start_point = (10,10)
end_point = (245,110)


color = (1 , 0, 255)

thickness = -5

image = cv2.rectangle(image , start_point , end_point , color ,thickness)

cv2.imshow("image" , image)





#rectangle


image = cv2.imread("pika.png")

start_point = (10,10)
end_point = (245,110)


color = (1 , 0, 255)

thickness = 5

image = cv2.rectangle(image , start_point , end_point , color ,thickness)

cv2.imshow("image" , image)




#line
image = cv2.imread("pika.png")

start_point = (0,0)
end_point = (5,10)


color = (1 , 0, 255)

thickness = 5

image = cv2.line(image , start_point , end_point , color ,thickness)

cv2.imshow("image" , image)





#circle
image = cv2.imread("pika.png")

center_coordinates = (100,50)
radius = 15
color = (0,0,255)
thickness = 2

image = cv2.circle(image , center_coordinates , radius , color ,thickness)

cv2.imshow("image" , image)


# filled circle
image = cv2.imread("pika.png")

center_coordinates = (100,50)
radius = 15
color = (0,0,255)
thickness = -2

image = cv2.circle(image , center_coordinates , radius , color ,thickness)

cv2.imshow("image" , image)





#text
image = cv2.imread("pika.png")

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50,50)
fontScale = 1
color = (0,0,255)
thickness = 2

image = cv2.putText(image ,'Opencv', font , fontScale, org , color ,thickness, cv2.LINE_AA)

cv2.imshow("image" , image)

cv2.waitKey()
cv2.destroyAllWindows()