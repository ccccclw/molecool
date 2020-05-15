"""
This module is for functions 

"""

import numpy as np

def calculate_distance(rA, rB):
    d=(rA-rB)
    dist=np.linalg.norm(d)
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta