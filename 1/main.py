import csv
import os
import modulos.votoswriter as votoswriter
import modulos.votosreader as reader

path = os.path.dirname(__file__)
listavotos = reader.reader(path)
votoswriter.gustavo(path, listavotos)