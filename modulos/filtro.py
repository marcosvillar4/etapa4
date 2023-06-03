def filtro(path, mayor):
    import csv
    import platform

    def segundo_item(lista):
        lista[1]

    if platform.system() == 'Windows':
        csvfile = path + ".\csv\\votos.csv"             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/votos.csv'

    votos_presidente = []
    cand1 = 0
    cand1 = mayor[0]
    cand1 = cand1[0]
    

    cand2 = 0
    cand2 = mayor[1]
    cand2 = cand2[0]

    
    
    with open(csvfile, "r") as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            clase_votos = int(row[2])
            if clase_votos == 1:
                if int(row[3]) == cand1 or int(row[3]) == cand2:
                    votos_presidente.append(row)

    return votos_presidente
