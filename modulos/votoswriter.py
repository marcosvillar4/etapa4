def gustavo(path, listavotos):
    import csv
    import platform
    import modulos.countysort as count

    if platform.system() == 'Linux':
        csvfile = path + '\csv'
    elif platform.system() == 'Windows':
        csvfile = path + '/csv'

    count(listavotos, path)
    with open (csvfile, 'w') as votos:
        writer = csv.writer(votos)


