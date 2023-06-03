
import os
import modulos.votoswriter as votoswriter
import modulos.votosreader as reader
import modulos.contador as contador
import modulos.writerresultados as resultados
import platform

path = os.path.dirname(__file__)
listavotos = reader.reader(path)
mayor = votoswriter.gustavo(path, listavotos)
cont1, cont2, contt, contb = contador.contvotos(path, mayor)
resultados.charles(path, cont1, cont2, contt, contb)
print('carlitos')