import cv2
import numpy as np 

img = cv2.imread("D:\\IEEE + IvLabs\\TechnoSeason 1\\IMAGES\\Lena.jpg") #change file path accordingly
img = cv2.resize(img,(300,300)) 
cv2.imshow("orignal",img)
#cv2.waitKey(0)
#images are cropped and stored as 9 other images 

img1 = img[0:100,0:100] 
img2 = img[0:100,100:200]
img3 = img[0:100,200:300]
img4 = img[100:200,0:100]
img5 = img[100:200,100:200]
img6 = img[100:200,200:300]
img7 = img[200:300,0:100]
img8 = img[200:300,100:200]
img9 = img[200:300,200:300]

parts =  np.array([img1,img2,img3,img4,img5,img6,img7,img8,img9]) #we made a numpy array to access them easily 

np.random.shuffle(parts) # shuffling each of puzzle's part randomly

img2 = np.zeros([300,300,3],np.uint8)*255 # creating black image 

 # function which copies one image on another, by which we can paste puzzle blocks on black image
 
def copy_img (img2,img1,m,n): 
    for i in range (0,100):
        for j in  range (0,100):
            img2[m+i][n+j] = np.add(img2[m+i][n+j],img1[i][j])
            #img2[m+i][n+j][1] = np.add(img2[m+i][n+j][1],img1[i][j][1])
            #img2[m+i][n+j][2] = np.add(img2[m+i][n+j][2],img1[i][j][2])        

copy_img(img2, parts[0], 0, 0)
copy_img(img2, parts[1], 0, 100)
copy_img(img2, parts[2], 0, 200)
copy_img(img2, parts[3], 100, 0)
copy_img(img2, parts[4], 100, 100)
copy_img(img2, parts[5], 100, 200)
copy_img(img2, parts[6], 200,0)
copy_img(img2, parts[7], 200, 100)        
copy_img(img2, parts[8], 200, 200)

#creatinng black board where our new puzzle will pe placed 

board = np.zeros([300,300,3],np.uint8)*255 

cv2.imshow("image",img2) #showing shuffled image 
#cv2.waitKey(0)

cv2.imshow("board",board) # showing black image
cv2.waitKey(0)

print("INDEXING IS DONE ACCORDING TO :-\n1 2 3 \n4 5 6\n7 8 9") #our method of indexing

#beacuse size of our puzzle is 300x300 we are using 100 and 200 to diffrentiate b/w the images 

for k in range (0,9):
    index1 = int(input("Enter index1 :- "))
    index2 = int(input("Enter index2 :- "))
    
    if(index2 == 1 ):
        copy_img(board, parts[index1-1],0,0) #index1-1 bcoz indexing starts from 1 
    if(index2 == 2 ):
        copy_img(board, parts[index1-1],0,100)
    if(index2 == 3 ):
        copy_img(board, parts[index1-1],0,200)
    if(index2 == 4 ):
        copy_img(board, parts[index1-1],100,0)
    if(index2 == 5 ):
        copy_img(board, parts[index1-1],100,100)
    if(index2 == 6 ):
        copy_img(board, parts[index1-1],100,200)
    if(index2 == 7 ):
        copy_img(board, parts[index1-1],200,0)
    if(index2 == 8 ):
        copy_img(board, parts[index1-1],200,100)
    if(index2 == 9 ):
        copy_img(board, parts[index1-1],200,200)  
       
    cv2.imshow("board",board) 
    cv2.waitKey(300)

flag = 0 # flag becomes 1 when we win 

if np.shape(img) == np.shape(board): # if they are of same size, dimensions 
    difference = cv2.subtract(img, board) # simply subtract from each pixel of the first image(img), the value of the corresponding pixel in the second image(board).
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("Congratulation! You have completely solved the puzzle !!")
        flag = 1 
    
if (flag == 0):
    print("TRY AGAIN !")

cv2.waitKey(0)
cv2.destroyAllWindows()



