def countysort(lista):
    import modulos.inforeader as info
    votoscount = []
    listaord = [] 
    listaord = sorted(lista, key=info(4))
    print(listaord)
    
        