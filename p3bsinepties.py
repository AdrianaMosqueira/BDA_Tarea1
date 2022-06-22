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
    comm.send(chunk1, dest=1,tag=1)
    comm.send(chunk2, dest=2,tag=2)
elif rank == 1:
    chunk11 = comm.recv(source=0,tag=1)
    max11=chunk11.max()
    comm.send(max11, dest=3)
    print("El procesador", rank,"encontró",max1)
elif rank == 2:
    chunk22 = comm.recv(source=0)
    max22=chunk22.max()
    comm.send(max22, dest=3)
    print("El procesador", rank,"encontró",max2)
elif rank == 3:
    max11 = comm.recv(source=1)
    max22 = comm.recv(source=2)
    max3=max(max1,max2)
    print("El procesador",rank,"encontró",max3)
