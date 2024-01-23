# Image Histogram Equalization
Histogram equalization is a method used in image analysis for enhancing and make easier to read difficult images. 
It's usually associated with an increase in contrast.

## How it works
It converts your image in black and white, then trasnsforms it in an array through the pillow library. Each pixel is processed using this formula:

$$<math>\displaystyle y{'} = \frac {CDF(y) − CDFmin} {L^2 - CDFmin} \cdot255</math>$$

where $CDF(y)$ is the cumulative sum of the all the pixel with the value in the domain $x \in [0, y]$ and $y$ is the pixel value.

For a basic demo, check the [Demo](/Demo) folder, while for more info check [this wikipedia article](https://en.wikipedia.org/wiki/Histogram_equalization).

## How to run
Download the files image-equalizer.py and Car.jpg and load the first one in your IDE or run it thorugh this coomand in your console:

``python3 image-equalizer.py``

Make sure Car.jpg is in your project directory and check if you have installed all the packages required.

