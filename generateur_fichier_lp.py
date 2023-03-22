with open("6I2",'r', encoding = 'utf-8') as f: #ouverture du fichier en mode lecture
    l = f.readlines() #lecture des lignes du fichier que l'on met dans une liste l
    l=[s.replace('\n', '') for s in l] #on se debarasse du caractere saut de ligne pour tous ls items de la liste
    x=[]
    for i in l[0].split(' ') :#On se debarasse des vides entre les nombres
        if i != '':
            x.append(i)
    nbr_e , nbr_couples , cap = [int(i) for i in x] # recuperation du nbr des elements, de couples et de la capcite du sac
    del(l[:2]) #On supprimme la premiere ligne notre liste l, ainsi que la deuxieme ne contenant qu'un saut de ligne
    profits = []
    profits_temp = []
    poids = []
    poids_temp = []
    couples = []
    x=0
    #Recupertation des lignes de la matrices profit
    for i in range(int(int(nbr_e)/10)) :
        profits_temp.append(l[0])
        del(l[0])
    del[l[0]]

    #Transformer la matrice profit en ligne et se debarasser completement des tabulations
    for p in profits_temp :
        for x in p.split(' '):
            if x!='' :
                profits.append(x)

        #Recupertation des lignes de la matrices poids
    for i in range(int(int(nbr_e)/10)) :
        poids_temp.append(l[0])
        del(l[0])
    del[l[0]]
    #Transformer la matrice poids en ligne et se debarasser completement des tabulations
    for p in poids_temp :
        for x in p.split(' '):
            if x!='' :
                poids.append(x)

    #Recuperation des couples :
    x=[]
    for i in range(len(l)):
        for j in l[i].split(' ') :
            if j != '':
                x.append(j)
        couples.append(list([i for i in x]))
        x=[]
    
    #Ecriture du probleme dans le fichier resultat.lp
    with open("DCKP.lp",'w', encoding = "utf-8") as r1 :
        r1.write("enter dckp\n")
        r1.write("Max\n")
        r1.write("obj:\n")
        r1.write(str(profits[0])+'x1')
        for i in range(1,len(profits)) :
            r1.write("+"+str(profits[i])+"x"+str(i+1))
        r1.write('\nst')
        r1.write("\nc1: ")
        r1.write(str(poids[0])+'x1')
        for i in range(1,len(poids)) :
            r1.write("+"+str(poids[i])+"x"+str(i+1))
        r1.write("<="+str(cap))
        r1.write('\nc2: x'+couples[0][0]+"+x"+couples[0][1]+"<=1")
        for i in range(1,nbr_couples):
            r1.write("\nc"+str(i+2)+": x"+couples[i][0]+"+x"+couples[i][1]+"<=1")
        #r1.write()
        r1.write("\nbounds")
        for i in range(1,nbr_e+1) :
            r1.write('\n0<=x'+str(i)+"<=1")
            pass
        r1.write("\nend")