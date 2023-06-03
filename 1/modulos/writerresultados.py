def charles(path, cont1, cont2, contt, cantb):
    import platform
    import csv
    import modulos.porcent2 as porc

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
                        if contt != 0:
                                        
                            porcblanco = porc.porcent(cantb,contt)
                            csvwriter.writerow([f"Votos en blanco: {cantb}",f" porcentaje % : {porcblanco}"])
                            porcpat1 = porc.porcent(cont1, contt)
                            csvwriter.writerow([f"Porcentaje votos partido nro 1: {porcpat1},  nro de votos: {cont1}"])

                            porcpat2 = porc.porcent(cont2, contt)
                            csvwriter.writerow([f"Porcentaje votos partido nro 2: {porcpat2}, nro de votos: {cont2}"])
                            porcpositivo = porc.porcent(contt - cantb,contt)
                            csvwriter.writerow([f"Votos positivos: {contt - cantb}",f" porcentaje % : {porcpositivo}"])
                            porcpat1 = porc.porcent(cont2, contt)
                            csvwriter.writerow([f"Votos totales: {contt}"])

                            porctotal = porc.porcent(contt, acuvotos)
                            csvwriter.writerow([f"Porcentaje de votos comparado a todas las provincias: {porctotal}"])

                