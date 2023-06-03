def gustavo(path, listavotos):
    import csv
    import platform
    import modulos.countysort as count
    import modulos.filtro as filtro
    import random

    if platform.system() == 'Linux':
        csvfile = path + '\csv\\votosfiltrados.csv'
    elif platform.system() == 'Windows':
        csvfile = path + '/csv/votosfiltrados.csv'

    mayor = count.countysort(path, listavotos)
      
    filtrado = filtro.filtro(path, mayor)
    
    random.shuffle(filtrado)
        
        
    
    with open (csvfile, 'w') as votos:
        writer = csv.writer(votos)
        writer.writerows(filtrado)


