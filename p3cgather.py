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
    tarea2_chunk = np.array_split(tarea2, 3)
    comm.Scatter(tarea2_chunk,chunk,root=0)
elif rank == 1:
    chunk = np.empty(349525)    
    max1=chunk.max()
    #comm.Send(max1, dest=0)
    print("El procesador", rank,"encontró",max1)
elif rank == 2:
    chunk = np.empty(349525)
    max2=chunk.max()
    #comm.Send(max2, dest=0)
    print("El procesador", rank,"encontró",max2)
elif rank == 3:
    chunk = np.empty(349525)
    max3=chunk.max()
    #comm.Send(max3, dest=0)
    print("El procesador", rank,"encontró",max3)
