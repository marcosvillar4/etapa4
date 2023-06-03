def contvotos(path, mayor):
    import csv
    import platform

    cont1 = 0
    cont2 = 0
    conttotal = 0

    cand1 = 0
    cand1 = mayor[0]
    cand1 = cand1[0]
    

    cand2 = 0
    cand2 = mayor[1]
    cand2 = cand2[0]

    
    
    if platform.system() == 'Windows':
        csvfile = path + ".\csv\\votosfiltrados.csv"
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/votosfiltrados.csv'

    with open(csvfile, "r") as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            if row != []:
                rowactual = int(row[3])
                            
                conttotal = conttotal + 1
                if rowactual == cand1:
                    cont1 = cont1 + 1
                if rowactual == cand2:
                    cont2 = cont2 + 1
    
    return cont1, cont2, conttotal