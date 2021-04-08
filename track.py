from math import sqrt

import cv2
from scipy.optimize import linear_sum_assignment

from Item import *


def distance(u, v):
    return sqrt(np.sum(np.square(u - v)))


def generateScoreMatrix(current, next):
    scoreMat = []
    for c in current:
        row = []
        for n in next:
            row.append(distance(c, n))
        scoreMat.append(np.array(row))
    return np.array(scoreMat)


def track(frame, measurements, items, threshold=30):
    map = {}
    next = []
    for idx, f in enumerate(items.keys()):
        next.append(items[f].getPred())
        map[idx] = f
    score = generateScoreMatrix(next, measurements)
    matching = linear_sum_assignment(score)
    indices = list(range(len(measurements)))
    for i, j in zip(matching[0], matching[1]):
        f = items[map[i]]
        if score[i][j] < threshold:
            indices.remove(j)
            path = f.update(measurements[j])
            for i in range(len(path) - 1):
                cv2.circle(frame, tuple(path[i].astype(np.int32)), 2, f.color)
                cv2.circle(frame, tuple(path[i + 1].astype(np.int32)), 2, f.color)
                cv2.line(frame, tuple(path[i].astype(np.int32)), tuple(path[i + 1].astype(np.int32)), f.color,
                         thickness=2)
        else:
            del items[map[i]]
    for leftover in indices:
        new = item(measurements[leftover])
        items[new.id] = new
    return frame, items
