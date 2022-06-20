from mpi4py import MPI

import numpy as np
import random
from numpy import genfromtxt

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    tarea2 = genfromtxt('tarea2.csv', delimiter=',')
    maximo = tarea2.max()
    print(maximo)
