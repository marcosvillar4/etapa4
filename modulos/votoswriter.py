def gustavo(path, listavotos):
    import csv
    import platform
    import modulos.countysort as count
    import modulos.filtro as filtro

    if platform.system() == 'Linux':
        csvfile = path + '\csv'
    elif platform.system() == 'Windows':
        csvfile = path + '/csv'

    mayor = count.countysort(path, listavotos)
    
    print(mayor)
    
    filtrado = filtro.filtro(path, mayor)
    
    print(filtrado)
    
    with open (csvfile, 'w') as votos:
        writer = csv.writer(votos)


