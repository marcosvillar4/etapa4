def csvfilewriter(path):
    import os
    import csv
    import platform
    import modulos.regiones2 as reg
    import modulos.countysort as cys
    import modulos.formato as formato
    import modulos.porcent2 as porc

    votprov = []
    acuvotos = 0

    path = os.path.dirname(__file__)

    if platform.system() == 'Windows':
        csvfile = path + f"\csv\\csv_regiones\csv_"             # Fix para windows y linux
    elif platform.system() == 'Linux':
        csvfile = path + f'/csv/csv_regiones/csv_'

    csvprov = csvfile + "provincias.csv"

    header1 = ["ELECCIONES GENERALES 2023"]
    body1 = ["Nro De lista", " Partido politico", " Votos", " Porcentaje % "]


    with open (csvprov, "r") as provincias:
        csvreader = csv.reader(provincias)
        for row in csvreader:
            rowactual = str.casefold(row[0])
            rowactual = rowactual.replace(" ", "_")
            csvfilereg = (csvfile + rowactual + f".csv")
            
            with open(csvfilereg, "w", ) as provwrite:
                csvwriter = csv.writer(provwrite)
                csvwriter.writerow([row[0]])
                votprov = reg.region2(path,int(row[1]), resp)
                listorden = cys.count(path, votprov)
                votos, votosblanco, votostotal = formato.formato(path, listorden)
                
                csvwriter.writerow(header1)
                csvwriter.writerow(body1)
                acuvotos = acuvotos + votostotal
                csvwriter.writerows(votos)
                if votostotal != 0:
                                        
                    porcblanco = porc.porcent(votosblanco,votostotal)
                    csvwriter.writerow([f"Votos en blanco: {votosblanco}",f" porcentaje % : {porcblanco}"])
                    porcpositivo = porc.porcent(votostotal - votosblanco,votostotal)
                    csvwriter.writerow([f"Votos positivos: {votostotal - votosblanco}",f" porcentaje % : {porcpositivo}"])

                    csvwriter.writerow([f"Votos totales: {votostotal}"])

                    porctotal = porc.porcent(votostotal, acuvotos)
                    csvwriter.writerow([f"Porcentaje de votos comparado a todas las provincias: {porctotal}"])

            
                
                

            
    
            
    
            

