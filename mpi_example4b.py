from mpi4py import MPI

import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    num1 = np.random.random(1000000, dtype=np.float)
    num2 = np.random.random(1000000, dtype=np.float)
    print (num1,num2)
