def countysort(path, listavotos):
    import modulos.inforeader as info
    import csv
    import platform

    

    def segundo_item(lista):
        return lista[1]
    
    def cuarto_item(lista):
        return int(lista[3])
    
    

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\partidos.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/partidos.csv'

    partid = []
    desorden = []
    orden = []
    with open (csvfile, "r") as partidos:
        reader = csv.reader(partidos)
        for row in reader:
            partid.append(int(row[2]))
    
    votospar = []
    for item in range(0, len(listavotos)):
        votospar.append(cuarto_item(listavotos[item]))

    for item in range(0, len(partid)):
        desorden.append([int(partid[item]),votospar.count(int(partid[item]))])
        
    
    orden = sorted(desorden, key=segundo_item, reverse=True)
    mayor2 = []
    mayor2.append(orden[0])
    mayor2.append(orden[1])

    return mayor2
    