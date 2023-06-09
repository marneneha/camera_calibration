import numpy as np
from pprint import pprint
twod_points = np.array([[757,213],[758,415],[758,686],[759,966],[1190,172], [329, 1041], [1204, 850], [340, 159]])
threed_points = np.array([[0,0,0,1], [0,3,0,1],[0,7,0,1], [0,11,0,1], [7,1,0,1], [0,11,7,1], [7,9,0,1], [0,1,7,1]])
# pprint(twod_points)
# pprint(threed_points)
A=np.empty([1,12], dtype=int)
for i in range(len(twod_points)):
    temp1 = np.matrix(np.concatenate([threed_points[i], np.zeros(4, dtype = int), -twod_points[i,0]*threed_points[i]]))
    temp2 = np.matrix(np.concatenate([np.zeros(4, dtype = int), threed_points[i], -twod_points[i,1]*threed_points[i]]))
    temp= np.concatenate((temp1,temp2), axis=0)
    pprint(temp)
    A = np.concatenate((A,temp), axis=0)
A = np.delete(A,0,0)
pprint(A)
# A = np.delete(A,0,0)
# Matrix = A.T*A
# pprint(A)
# pprint(Matrix)
# w, v = np.linalg.eig(Matrix)
# print(w,v)
# print("p matrix is",v[0])
# print(np.around(10*v[0]))
# print(np.mean(v[0]))
u, s, vh = np.linalg.svd(A)
P = vh[-1,:] 
print("p matrix is", P)
# print("u is",u)
# print("s is",s)
# print("vh is",vh)