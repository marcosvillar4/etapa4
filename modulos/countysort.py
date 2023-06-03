def countysort(path, listavotos):
    import modulos.inforeader as info
    import csv
    import platform

    print(listavotos)

    def segundo_item(lista):
        return lista[1]

    if platform.system() == 'Windows':
        csvfile = path + "\csv\\partidos.csv"           # Fix para linux
    elif platform.system() == 'Linux':
        csvfile = path + '/csv/partidos.csv'


    partid = []
    with open (csvfile, "r") as partidos:
        reader = csv.reader(partidos)
        for row in reader:
            partid.append(int(row[2]))

    cantvotos = []
    for i in range(0, len(partid)):
        cantvotos.append([int(partid[i]),listavotos.count(int(partid[i]))])

    print(cantvotos)

    orden = sorted(cantvotos, key=segundo_item(cantvotos))

    mayor2 = []
    mayor2.append(orden[0])
    mayor2.append(orden[1])

    print(mayor2)