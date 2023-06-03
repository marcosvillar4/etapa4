def countysort(lista, path):
    import modulos.inforeader as info
    import csv
    import platform

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\partidos.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/partidos.csv'


    partid = []
    with open (csvfile, "r") as partidos:
        reader = csv.reader(partidos)
        for row in reader:
            partid.append(row[2])

    cantvotos = []
    for i in range(0, len(partid)):
        cantvotos.append([int(partid[i]),lista.count(partid[i])])

    orden = sorted(cantvotos, key=info.inforeader(1, cantvotos))

    mayor2 = []
    mayor2.append(orden[0])
    mayor2.append(orden[1])

    print(mayor2)