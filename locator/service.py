from scipy.spatial import distance
import numpy as np

import logging

logger = logging.getLogger('django')


class Locator:
    points = ''
    adjuscent = ''

    def __init__(self, points):
        self.points = points

    def get_adjuscent_points(self):

        # tree = spatial.KDTree(self.points)

        coords = np.array(self.points)
        distances = distance.cdist(coords, coords, 'euclidean')
        np.fill_diagonal(distances, np.inf)

        min_index = (np.argmin(distances))
        closest = np.unravel_index(min_index, distances.shape)
        
        logger.info("self.points =======>>")
        logger.info(f"The two closest are {closest}")
        logger.info(f"They are at distance {distances[closest]}")
        logger.info(f"Resp. coordinates {coords[closest[0]]} and {coords[closest[1]]}")
        return coords[closest[0]], coords[closest[1]]
        

        # logger.info( A[ tree.query((0.5,0.5,0.5,0.5,0.5))[1] ])
