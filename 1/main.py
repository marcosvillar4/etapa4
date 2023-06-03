
import os
import modulos.votoswriter as votoswriter
import modulos.votosreader as reader
import modulos.contador as contador
import modulos.writerresultados as resultados
import platform

path = os.path.dirname(__file__)
listavotos = reader.reader(path)
votoswriter.gustavo(path, listavotos)
print('carlitos')