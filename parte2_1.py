from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    diccionario1 = {'alpha': 3, 'beta': 1.5}
    comm.send(diccionario1, dest=1 , tag=1)
    diccionario2 = {'Meses': 12, 'Días': 30}
    comm.send(diccionario2, dest=2 , tag=2)
    diccionario3 = {'Edad': 23, 'Grupo':5 }
    comm.send(diccionario3, dest=3 , tag=3)
elif rank == 1:
    diccionario1 = comm.recv(source=0 , tag=1)
    print("I am processor", rank)
    print(diccionario1)   
elif rank == 2:
    diccionario2 = comm.recv(source=0 , tag=2)
    print("I am processor", rank)
    print(diccionario2)   
elif rank == 3:
    diccionario3 = comm.recv(source=0 , tag=3)
    print("I am processor", rank)
    print(diccionario3)
