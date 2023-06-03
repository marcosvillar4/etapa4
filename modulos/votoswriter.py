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
    votosmayor = filtro.filtro(path, mayor)
    with open (csvfile, 'w') as votos:
        writer = csv.writer(votos)


