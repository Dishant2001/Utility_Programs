import cv2 as cv
# from matplotlib import pyplot as plt
# from matplotlib.lines import Line2D
import numpy as np
# from data_extract import getEmails


# name_list=['Dishant Kumar','Sonali Bedade','Pranav Khatal', 'Parth Yadav','Batman Begins']
name_list=getEmails('gfg')[1]
# print(name_list)


cv.namedWindow("certificate", cv.WINDOW_NORMAL)
cv.resizeWindow('certificate',960,540)
point_matrix = np.zeros((2,2),np.int)
 
counter = 0
def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:
        point_matrix[counter] = x,y
        counter = counter + 1

img=cv.imread('images/test_cert.png')


# while True:
#     for x in range (0,2):
#         cv.circle(img,(point_matrix[x][0],point_matrix[x][1]),3,(0,0,255),cv.FILLED)
 
#     if counter == 1:
#         starting_x = point_matrix[0][0]
#         starting_y = point_matrix[0][1]
 
#         # ending_x = point_matrix[1][0]
#         # ending_y = point_matrix[1][1]
#         # cv.rectangle(img, (starting_x, starting_y), (ending_x, ending_y), (0, 255, 0), 3)
 
#     cv.imshow("certificate", img)

#     cv.setMouseCallback("certificate", mousePoints)
#     print(point_matrix)
#     if cv.waitKey(1)==27:
#         break

while True:
    for x in range (0,2):
        cv.circle(img,(point_matrix[x][0],point_matrix[x][1]),3,(0,0,255),cv.FILLED)
 
    if counter == 2:
        starting_x = point_matrix[0][0]
        starting_y = point_matrix[0][1]
 
        ending_x = point_matrix[1][0]
        ending_y = point_matrix[1][1]
        cv.rectangle(img, (starting_x, starting_y), (ending_x, ending_y), (0, 0, 255), 5)
 
    cv.imshow("certificate", img)

    cv.setMouseCallback("certificate", mousePoints)
    print(point_matrix)
    if cv.waitKey(1)==27:
        break


cv.destroyAllWindows()
print(point_matrix)
cv.namedWindow("certificate", cv.WINDOW_NORMAL)
cv.resizeWindow('certificate',960,540)

# name='Dishant Kumar'
font=cv.FONT_HERSHEY_DUPLEX
scale=7
thickness=10
color=(0,0,0)
for name in name_list:
    textsize=cv.getTextSize(name,font,scale,thickness)
    print('Text Size: ',textsize)
    textX = int(point_matrix[1][0]-point_matrix[0][0] - (textsize[0][0]))
    # textY = int(point_matrix[1][1]-point_matrix[0][1] + (textsize[1][0] / 2))

    final_img=cv.putText(cv.imread('images/test_cert.png'),name,(point_matrix[0][0]+int(textX/2),point_matrix[0][1]+130),font,scale,color,thickness)

    # final_img=cv.putText(cv.imread('images/test_cert.png'),'Dishant Kumar',(point_matrix[0][0]+70,point_matrix[0][1]+50),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,2.5,(0,0,0),4,cv.LINE_AA)
    # cv.imshow('final certificate',final_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite('images/'+name+'.png'.format(name),final_img)
