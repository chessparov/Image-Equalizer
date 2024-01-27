# Image Histogram Equalization
Histogram equalization is a method used in image analysis for enhancing and to make easier to read difficult images as X-Rays or aerial pictures. 
It's usually associated with an increase in contrast.

## How it works
It converts your image in black and white, then trasnsforms it in an array through the pillow library. Each pixel is processed using this formula:

$$<math>\displaystyle y{'} = \frac {CDF(y) − CDFmin} {L^2 - CDFmin} \cdot255</math>$$

where $CDF(y)$ is the cumulative sum of the all the pixels with the value in the domain $x \in [0, y]$ and $y$ is the pixel value.

For a basic demo, check the [demo](/Demo) folder, while for more info check [this wikipedia article](https://en.wikipedia.org/wiki/Histogram_equalization).

**Note:** All the most common formats are accepted and there's not limitation on image size. All images provided will be converted to black and white though.

## How to run
Download the files "image-equalizer.py" and "test_image.JPG"; then load the first one in your IDE or run it thorugh this coomand in your console:

``$ python3 image-equalizer.py``

Make sure "Car.jpg" is in your project directory and check if you have installed all the packages required. If you are having trouble running through terminal the above command because of missing packages, install them using:

``$ pip install "package-name"``


