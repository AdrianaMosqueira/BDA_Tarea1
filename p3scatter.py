from mpi4py import MPI

import numpy as np
import pandas as pd
import random
from numpy import genfromtxt


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

tarea2 = genfromtxt('tarea2.csv', delimiter=',')
tarea2_chunks = np.array_split(tarea2, 3)

if rank == 0:
    data = tarea2_chunks 
else:
    data=np.empty(349525)
comm.Scatter(data,root=0)
