from mpi4py import MPI

import numpy as np
import pandas as pd
import random
from numpy import genfromtxt


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    tarea2 = genfromtxt('tarea2.csv', delimiter=',')
    tarea2_chunk = np.array_split(tarea2, 2)
    chunk1=tarea2_chunk[0]
    chunk2=tarea2_chunk[1]
    comm.Send(chunk1, dest=1)
    comm.Send(chunk2, dest=2)
elif rank == 1:
    chunk1 = np.empty(524288)
    comm.Recv(chunk1, source=0)
    max1=chunk1.max()
    comm.Send(max1, dest=2)
elif rank == 2:
    chunk2 = np.empty(524287)
    comm.Recv(chunk2, source=0)
    max2=chunk2.max()
    comm.Send(max2, dest=2)
elif rank == 3:
    max3 = np.empty(2)
    comm.Recv(max1, source=1)
    comm.Recv(max2, source=2)
    maxfin=max3.max()
    print(maxfin)
