def contvotos(path):
    import csv
    import platform

    cont1 = 0
    cont2 = 0
    conttotal = 0

    if platform.system() == 'Windows':
        csvfile = path + ".\csv\\votosfiltrados.csv"
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/votosfiltrados.csv'

        with open(csvfile, "r") as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                clase_votos = int(row[3])
                conttotal = conttotal + 1
                if clase_votos == 1:
                    cont1 = cont1 + 1
                if clase_votos == 2:
                    cont2 = cont2 + 1
    
    return cont1, cont2, conttotal