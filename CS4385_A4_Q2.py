import cv2
import numpy as np
from multiprocessing import Pool, freeze_support
import time

def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened

def process_image_piece(img_idx_r_c_dir):
    image, i, nr, nc, output_dir = img_idx_r_c_dir

    x = i % nc

    y = i // nc

    height = image.shape[0]//nr
    width = image.shape[1]//nc

    part = image[y*height:(y+1)*height, x*width:(x+1)*width]

    sharpened_part = sharpen_image(part)

    cv2.imwrite(output_dir + f"splitt_{x}_{y}.png", sharpened_part)

    return y, x, sharpened_part

if __name__ == "__main__":
    
    freeze_support() # stops my warning messages 

    for n_processors in range(1,7): # trying multiple processors

        print('\nStarting: ' + str(n_processors))

        rawimage = cv2.imread("C:/Users/apant/Downloads/CS4385_A4/WT_WilderPark.jpg") # Raw image - WT baseball field

        split_images_dir = "C:/Users/apant/Downloads/CS4385_A4/WT_split/"


        pool = Pool(processes=n_processors)
        
        passers = []

        for idx in range(900): # putting process pieces in a list to give to processors
            passer = (rawimage, idx, 30, 30, split_images_dir)
            passers.append(passer)

        start_time = time.time()
        
        pool.map(process_image_piece, passers)
        pool.close()
        pool.join()

        print(f"Split took {time.time() - start_time} seconds with {n_processors} processors")
        
        parts = []

        for y in range(30):
            row_parts = []

            for x in range(30):
                part_path = split_images_dir+ f"splitt_{x}_{y}.png"
                part = cv2.imread(part_path)
                row_parts.append(part)
            
            concatenated_rows = []

            for i in range(len(row_parts[0])):
                new_row = []
                for part in row_parts:
                    new_row.extend(part[i])  
                concatenated_rows.append(new_row)

            parts.append(concatenated_rows)
        
        final_image = []
        for part in parts:
            final_image.extend(part)  

        final_image = np.array(final_image)


        cv2.imwrite("C:/Users/apant/Downloads/CS4385_A4/WT_split/sharp_WT_ballpark.jpg", final_image)
