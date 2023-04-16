import numpy as np
from pprint import pprint
twod_points = np.array([[757,213],[758,415],[758,686],[759,966],[1190,172], [329, 1041], [1204, 850], [340, 159]])
threed_points = np.array([[0,0,0,1], [0,3,3,1],[0,7,0,1], [0,11,0,1], [7,1,0,1], [0,11,7,1], [7,9,0,1], [0,1,7,1]])
pprint(twod_points)
pprint(threed_points)
A=np.empty([1,12], dtype=int)
for i in range(len(twod_points)):
    temp1 = np.matrix(np.concatenate([threed_points[i], np.zeros(4, dtype = int), -twod_points[i,0]*threed_points[i]]))
    temp2 = np.matrix(np.concatenate([np.zeros(4, dtype = int), threed_points[i], -twod_points[i,1]*threed_points[i]]))
    temp= np.concatenate((temp1,temp2), axis=0)
    pprint(temp)
    A = np.concatenate((A,temp), axis=0)
A = np.delete(A,0,0)
pprint(A)