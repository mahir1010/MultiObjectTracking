# Multi Object Tracking

Mahir Patel  
Navoneel Ghosh  

2021.4.8


* * *

## Overall Description

We use computer vision techniques to localize and track multiple objects in a video

* * *

## Method and Implementation

Our process starts with background subtraction to perform motion segmentation. We perform median blur with kernel size 3 to remove isolated white pixels from the background. After that we perform gaussian blur and dilation of image further. After thresholding that image, we find contours in the image and only keeping the ones with high enough area. We maintain Kalman Filter for each object and use Hungarian algorithm for data association. The decision process is naive as we assume that if our Kalman prediction is far from measurement, i.e. after matching the score is higher than a specific threshold, we delete the old track and create a new one. The output can be improved by tuning Kalman filters and changing decision algorithm.

Additionally, for the cell dataset, we generated a mask to keep only the petri dish in the video.

* * *
## Data
[Test videos stored as numpy arrays can be found at this link](https://drive.google.com/drive/folders/1PpnpIkjnl1Xbt9-xdW64R2s65CXN50lE?usp=sharing)

* * *

## Results

![](images/bats.gif)
![](images/cells.gif)

* * *

## Discussion

**Strengths:**
*  In the cell dataset, our detection is very accurate. Tracking is also robust given cells do not jump around a lot

**Limitations:**
*   The data association algorithm is not very robust. Most of the time we opt for creating a new track.

* * *

## Credits and Bibliography 
[Kalman Filter](https://nbviewer.jupyter.org/github/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/table_of_contents.ipynb)

[Opencv-python](https://opencv-python-tutroals.readthedocs.io/en/latest/)

* * *
 
