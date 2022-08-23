import numpy as np 

a = np.load('data/sparseMatrix1.npy')
b = np.load('data/sparseMatrix2.npy')

arr = np.concatenate((a, b), axis=0)

origarr = np.load('data/sparseMatrix.npy')

# try fix this 
# assert arr == origarr

