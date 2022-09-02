import numpy as np

arr = np.load('data/sparseMatrix.npy')

np.split(arr, 2)

file = 1

for split in (np.split(arr, 2)):
    np.save(f"data/sparseMatrix{file}.npy", split)
    file += 1

