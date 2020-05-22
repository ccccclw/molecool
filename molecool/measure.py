"""
This module is for functions 

"""

import numpy as np

def calculate_distance(rA, rB):
    """
    Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Return 
    ------
    distance : float
        The distance between the two points
    
    Examples
    --------
    >>> r1 = np.array([0.0,0.0,0.0])
    >>> r2 = np.array([0.0,0.0,0.0])
    >>> calculate_dist(r1, r2)
    1.0
    """
    if isinstance(rA, np.ndarray) is False or isinstance(rB, np.ndarray) is False:
        raise TypeError("input should be numpy array")
    d=(rA-rB)
    distance=np.linalg.norm(d)
    if distance == 0.0:
        raise Exception("Two atoms are in the same point")
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    """
    Calculate the angle given three coordinates.

    Parameter
    ---------
    rA, rB, rC : np.ndarray
        The coordinates of each point.

    Return
    ______
    angle : float
        The angle given three coordinates
    """
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
