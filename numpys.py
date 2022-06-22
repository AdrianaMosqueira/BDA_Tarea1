from mpi4py import MPI

import numpy as np
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    random.seed (1102)
    num1 = np.random.random(1000000)
    num2 = np.random.random(1000000)
    print ("El array num1 generado por el procesador",rank,"es",num1)
    print ("El array num2 generado por el procesador",rank,"es",num2)
