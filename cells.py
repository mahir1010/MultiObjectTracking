import cv2

from Item import *
from track import track

if __name__ == '__main__':
    vid = np.load(open('./cell.npy', 'rb'))
    mask = cv2.imread('./mask.png', 0)
    bgS = cv2.createBackgroundSubtractorMOG2()
    writer=cv2.VideoWriter('Cells.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10.0, (vid[0].shape[1],vid[0].shape[0]))
    tracking = None
    for INDEX, frame in enumerate(vid):
        fgmask = cv2.bitwise_and(frame, frame, mask=mask)
        fgmask = cv2.GaussianBlur(fgmask, (5, 5), 1.4)
        fgmask = bgS.apply(fgmask)
        if INDEX < 2:
            continue
        fgmask[fgmask > 0] = 255
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, np.ones((7, 7)))
        contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cells = []
        for c in contours:
            M = cv2.moments(c)
            if M['m00'] > 100:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cells.append(np.array([cX, cY]))
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if tracking is None:
            tracking = {}
            for c in cells:
                i = item(c)
                tracking[i.id] = i
                cv2.circle(frame, tuple(c), 2, i.color)
        else:
            frame, tracking = track(frame, cells, tracking, 70)
        cv2.imshow('cells', frame)
        writer.write(frame)
        if cv2.waitKey(80) == ord('q'):
            break
