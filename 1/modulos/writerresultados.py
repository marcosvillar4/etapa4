def charles(path, cont1, cont2, contt):
    import platform
    import csv

    acuvotos = 0
    if platform.system() == 'Windows':
        csvfile2 = path + f"\csv\\csv_regiones\csv_"             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile2 = path + f'/csv/csv_regiones/csv_'

    if platform.system() == 'Linux':
        csvfile = path + '\csv\\'
    elif platform.system() == 'Windows':
        csvfile = path + '/csv/'

    csvprov = csvfile + "provincias.csv"

    header1 = ["ELECCIONES GENERALES 2023"]
    body1 = [f"Categoria: Presidente y Vicepresidente"]
    body2 = ["Nro De lista", " Partido politico", " Votos", " Porcentaje % "]

    with open (csvprov, "r", ) as provincias:
        csvreader = csv.reader(provincias)
        for row in csvreader:
            rowactual = str.casefold(row[0])
            rowactual = rowactual.replace(" ", "_")
            csvfilereg = (csvfile2 + rowactual + '.csv')

    

            with open(csvfilereg, "w", ) as provwrite:
                        csvwriter = csv.writer(provwrite)
                        csvwriter.writerow([row[0]])
                                        
                        csvwriter.writerow(header1)
                        csvwriter.writerow(body1)
                        csvwriter.writerow(body2)
                        acuvotos = acuvotos + contt
                