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
    data = np.array_split(tarea2, 3)
else:
    data_s=np.empty(349525)
comm.Scatter(data,data_s,root=0)
