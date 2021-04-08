import cv2
import numpy as np
import pandas as pd

from Item import item
from track import track

if __name__ == '__main__':
    df = pd.DataFrame(columns=['data', 'filtered'])
    video = np.load(open('./video.npy', 'rb'))
    segmentation = np.load(open('segmentation.npy', 'rb'))
    writer=cv2.VideoWriter('Bats.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10.0, (video[0].shape[1],video[0].shape[0]))
    tracking = None
    length = []
    prevTrack = None
    count = 0
    for frame, segmentedFrame in zip(video, segmentation):
        segmentedFrame = cv2.dilate(segmentedFrame, np.ones((2, 2)))
        segmentedFrame[segmentedFrame > 0] = 255
        contours, hierarchy = cv2.findContours(segmentedFrame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        bats = []
        for c in contours:
            M = cv2.moments(c)
            if M['m00'] > 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                bats.append(np.array([cX, cY]))
        if tracking is None:
            tracking = {}
            for b in bats:
                i = item(b)
                tracking[i.id] = i
                cv2.circle(frame, tuple(b), 2, i.color)
        else:
            frame, tracking = track(frame, bats, tracking)

        cv2.imshow('Bats', frame)
        writer.write(frame)
        if cv2.waitKey(40) == ord('q'):
            break
