import csv
import os
import modulos.votoswriter as votoswriter
import modulos.votosreader as reader
import modulos.votoswriter_formato as votosformato

path = os.path.dirname(__file__)
listavotos = reader.reader(path)
votoswriter.gustavo(path, listavotos)
votosformato.csvfilewriter(path)
print('carlitos')