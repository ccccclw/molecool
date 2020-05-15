"""
This module is for functions 

"""

import numpy as np

def calculate_distance(rA, rB):

    if isinstance(rA, np.ndarray) is False or isinstance(rB, np.ndarray) is False:
        raise TypeError("input should be numpy array")
    d=(rA-rB)
    dist=np.linalg.norm(d)
    if dist == 0.0:
        raise Exception("Two atoms are in the same point")
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta