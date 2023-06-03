def gustavo(path, listavotos):
    import csv
    import platform

    if platform.system() == 'Linux':
        csvfile = path + '\csv'
    elif platform.system() == 'Windows':
        csvfile = path + '/csv'


    with open (csvfile, 'w') as votos:
        writer = csv.writer(votos)
        
