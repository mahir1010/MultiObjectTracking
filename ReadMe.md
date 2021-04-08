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

![](https://github.com/mahir1010/MultiObjectTracking/blob/master/bats.gif?raw=true)
![](https://github.com/mahir1010/MultiObjectTracking/blob/master/cells.gif?raw=true)

* * *

## Discussion

1. If the motion is continuous and not spurious, our algorithm manages to generate long and stable tracks. Whereas, if the distance between Kalman prediction and measurement is more than certain threshold, we delete our old track and start a new one. Our tracker manages to handle new tracks and out of view tracks.
2. We have selected a specific threshold for both dataset. If the distance between Kalman prediction and measurement is higher than the threshold, we delete old track and create a new one.
3. Our filter uses constant velocity model, therefore if the object doesn't change direction rapidly after occlusion, our algorithm will work well. In that, it works well in the bat dataset but the cell dataset is very random.
4. We delete old track and create a new one.
5. We need the velocity model to better predict the frames. In fact we can also change this to constant acceleration model to have even more accurate results.

* * *

## Credits and Bibliography 
[Kalman Filter](https://nbviewer.jupyter.org/github/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/table_of_contents.ipynb)

[Opencv-python](https://opencv-python-tutroals.readthedocs.io/en/latest/)

* * *
 
