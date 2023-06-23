# -*- coding: utf-8 -*-
"""
This is a temporary script file.
"""

import cv2
#from PIL import Image
import skimage.io
#import tifffile
import os

# the path for the directory which contains the image files
in_dir="C:\\Users\\ali darbandi\\Documents\\python_files\\"

# the path to save the list of defocused images
out_dir="C:\\Users\\ali darbandi\\Documents\\python_files\\out_of_focus.txt"

blured_list=[]


def crop_ops(image_path):     #function to read the images and resize them
    
    image = cv2.imread(image_path,0)      #reading files
    
    image = cv2.resize(image, (500,500))  #down sampling to enhance the laplace variance
    
 # print("original image size is", image.shape)


# Display or save the cropped image
   # cv2.imshow("Cropped Image", image)
   # cv2.waitKey(0)
  #  cv2.destroyAllWindows()
    return image



def detect_blur(input_image):      #function to calculate the amount of image blure
    
    # Calculate the Laplacian variance
    laplacian_var = cv2.Laplacian(input_image, cv2.CV_64F).var()

    # Determine if the image is blurry based on the variance
    if laplacian_var < 1000:  # Adjust this threshold to control sensitivity
       
      blured_list.append(files)
      return "Blurry" , laplacian_var
        
    else:
      return "Not blurry", laplacian_var



for files in os.listdir(in_dir):   #looping through all images
                  
         path = in_dir + files

         #print(path)
# Detect blur in the image
         input_image=crop_ops(path)

         result, laplacian_var = detect_blur(input_image)

# Print the result0
         print("Image", files, "is" , result, "with Laplacian variance of ", "{:.1f}".format(laplacian_var) )

print(blured_list)

#save file list as a text document. delete the existing text file before rerunning the script. 
with open(out_dir, 'w') as file:
    file.write('\n'.join(blured_list))
















