import csv
import os
import modulos.votoswriter as votoswriter
import modulos.votosreader as reader
import modulos.contador as contador

path = os.path.dirname(__file__)
listavotos = reader.reader(path)
mayor = votoswriter.gustavo(path, listavotos)
cont1, cont2, conttotal = contador.contvotos(path, mayor)
print(cont1)
print(cont2)
print(conttotal)
print('carlitos')