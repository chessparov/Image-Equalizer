import numpy as np
from collections import defaultdict
from PIL import Image as im
import time


# Define some sample matrix for testing
image1 = np.array([[34, 45, 2, 123], [234, 23, 56, 99], [3, 88, 198, 34], [19, 77, 4, 200]], dtype=np.uint8)
image2 = np.array([[3, 2, 5, 2], [4, 3, 1, 1], [3, 1, 3, 1], [4, 1, 4, 3]], dtype=np.uint8)


def getCDF(image: np.ndarray):
    """Calculates CDF for each element of the matrix and saves the data in a dictionary"""
    dctOccurences = defaultdict(int)
    dctCDF = defaultdict(int)
    highest_bit = np.max(image)

    # Counts the occurences of each int value
    for i in range(0, highest_bit + 1):
        dctOccurences[i] = np.count_nonzero(image == i)

    # Counts the cumsum for each value (sum of the number of occurences of the value and all the smaller values)
    for k, v in enumerate(dctOccurences):
        for j in range(k + 1):
            dctCDF[k] += dctOccurences[j]

    # Eliminate all empty fields created by defaultdict
    to_be_eliminated = list()
    for k, v in enumerate(dctCDF):
        if dctCDF[k] == 0:
            to_be_eliminated.append(k)
    for k in to_be_eliminated:
        dctCDF.pop(k)

    return dctCDF

def getCDFmin(func):
    """

    Gets the smaller value of CDF

    """

    intMin = min(func.values())
    return intMin

# Assuming squared images
def equalizeImage(image: np.ndarray, size: int):
    """

    Apply the equalization to each pixel of the image

    """

    # Stores all the needed values separately in order to make simpler the for cicle
    dctCDF = getCDF(image)
    intMin = getCDFmin(dctCDF)
    intLSquared = (size)**2
    new_image = image.copy()

    for row in range(size):
        for col in range(size):
            pixel = new_image[row][col]
            new_image[row][col] = int((((dctCDF[pixel] - intMin)*255)/((intLSquared) - intMin)))
    return new_image

def processImage():
    """

    Gets the actual image, transforms it in black and white if necessary and stores
    the processed result along with the unprocessed for an easier comparison

    """

    # Importing real Image
    raw_image = im.open('Car.jpg')

    # Get the dimension of the image
    size = min(raw_image.size)

    # Cropping to get it square // Choose whether to crop or to resize
    # cropped_image = raw_image.resize((size, size))
    cropped_image = raw_image.crop((0, 0, size, size))

    # Transform it in black and white
    bw_image = cropped_image.convert('L')

    # Getting the matrix associated to the picture
    pixel_matrix = np.array(bw_image.getdata(), dtype=np.uint8)
    pixel_matrix = np.reshape(pixel_matrix, (size, size))

    # Saving both the processed and unprocessed pictures
    unprocessed_image = im.fromarray(pixel_matrix)
    unprocessed_image.save('Car_unprocessed.png')

    data_processed = equalizeImage(pixel_matrix, size)
    processed_image = im.fromarray(data_processed)
    processed_image.save('Car_processed.png')

    # Show the results
    unprocessed_image.show()
    processed_image.show()

######################################################################################################
# Main body
######################################################################################################

if __name__ == '__main__':

    start_time = time.time()

    processImage()

    print("\nRun time:\t\t--- %s seconds ---" % (round((time.time() - start_time), 5)))