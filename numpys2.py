from mpi4py import MPI

import numpy as np
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

np.random.seed(1102)

if rank == 0:
    num1 = np.random.random(1000000)
    num2 = np.random.random(1000000)
    comm.Send(num1, dest=1)
    comm.Send(num2, dest=2)
elif rank == 1:
    num1 = np.empty(1000000)
    comm.Recv(num1, source=0)
    print ("El procesador",rank,"recibio",num1)
elif rank == 2:
    num2 = np.empty(1000000)
    comm.Recv(num2, source=0)
    print ("El procesador",rank,"recibio",num2)
