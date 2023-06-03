
import os
import modulos.votoswriter as votoswriter
import modulos.votosreader as reader
import modulos.contador as contador
import modulos.writerresultados as resultados
import platform

path = os.path.dirname(__file__)
listavotos = reader.reader(path)
mayor = votoswriter.gustavo(path, listavotos)
cont1, cont2, conttotal = contador.contvotos(path, mayor)
print(cont1)
print(cont2)
print(conttotal)
if platform.system() == 'Windows':
    dirloc = path + f"\csv\\csv_regiones"          
elif platform.system() == 'Linux':
    dirloc = path + f'/csv/csv_regiones/'

if platform.system() == 'Windows':
    dirloc1 = path + f"\csv\\csv_regiones"           # Fix para linux
elif platform.system() == 'Linux':
    dirloc1 = path + f'/csv/csv_regiones'
try:
    os.mkdir(dirloc1, mode=0o777)
    
except:
    print("")

try:
    os.mkdir(dirloc, mode=0o777)
    

except:
    print('')
    
resultados.charles(path, cont1, cont2, conttotal)
print('carlitos')