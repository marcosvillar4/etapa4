def reader(path):
    import csv
    import platform

    if platform.system() == 'Windows':
        csvfile = path + ".\csv\\votos.csv"             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/votos.csv'

    votos_presidente = []

    with open(csvfile, "r") as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            clase_votos = int(row[2])
            if clase_votos == 1:
                votos_presidente.append(row)

    return votos_presidente
