from mpi4py import MPI

import numpy as np
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    random.seed (1102)
    num1 = np.random.random(1000000)
    num2 = np.random.random(1000000)
    print (num1,num2)
