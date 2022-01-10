from neuronio import neuro 
#analisador de padroes vai tentativa e errro
#ligacao armazena um vetor contendo o indice do neuronio, o indice de lig sera uma sequencia
redeN = []
# lig["SEQUENCIA"]=redeN[i]
# lig["SEQUENCIA"].[aprendizado] = neuronio.py
lig = {}
hist = ""
visivel = 1

def P(var):
    if visivel==1:
        print(var)

def Pense(E):
    global hist
    global lig
    global redeN
    # score armazenara as ocorrencias e servira para calculo de probabilidade
    #  score["VALOR PREVISTO"] = ([ocorrencias],[totais],[em],[redeN])
    # prev anotara a lista de previsoes
    # prev[i]<-lig[j] prev[i][i2]=neuronio()
    prev = []
    #chavePriv criado para nao precisar refazer o calculo das ligacoes com o historico,para criacao de nova ligacao com novo resultado
    ChavePrev = {}
    score = {}
    previC = ""
    #ARMAZENANDO NO HISTORICO    
    hist = hist + E
    #se for uma previsao aprendida
    if E in score:
        # encontrando valores pela referencia
        for i in range (0,len(prev),1):
            # verificando referencias
            for i2 in range (0,len(prev[i]),1):
                if redeN[prev[i][i2]].val == E:
                    #aumentando os pontos das previsoes corretas
                    redeN[prev[i][i2]].oco += 1
    elif len(hist) > 0:
        # Caso nao possua esse conhecimento sera criado
        id = len(redeN)
        redeN.append(neuro())
        redeN[id].oco += 1
        redeN[id].val = E
        print(redeN[id].val)
        print(redeN[id].oco)
        print(redeN[id].ref)
        #caso nao haja nada semelhante sera criado algumas ligacoes
        if len(prev) == 0:
            bit = 1
            while bit <= len(hist):
                #adcionando memoria do padrao
                lig[hist[len(hist)-bit-1:len(hist)-1]]=[]
                lig[hist[len(hist)-bit-1:len(hist)-1]].append(id)
                bit +=1
        else:
            # criando referencia as sequencicas
            for i in range (0,len(prev),1):
                lig[ChavePrev[str(i)]].append(id)
    arq = open('hist.txt','w')
    arq.write("<hist>\n")
    arq.write(hist+"\n")    
    if len(lig) != 0:
        for i in lig.keys():
            arq.write("\nlig['"+str(i)+"'] = ")
            if len(lig[i]) != 0:
                for i2 in range (0,len(lig[i]),1):
                    arq.write(" { "+str(lig[i][i2])+" } ")
    arq.close()        
    arq = open('rede.txt','w')
    arq.write("\n")
    if len(redeN) != 0:
        for i in range (0,len(redeN),1):
            arq.write("\nredeN[" + str(i) + "] = { val : " + redeN[i].val + " } , { oco : " + str(redeN[i].oco) + " }")
    arq.close()
    arq = open('relacionado.txt','w')
    arq.write("<hist>\n")
    arq.write(hist+"\n")
    if len(lig) != 0:
        for i in lig.keys():
            arq.write("\nlig['"+str(i)+"'] = ")
            if len(lig[i]) != 0:
                for i2 in range (0,len(lig[i]),1):
                    arq.write(" { v:"+str(redeN[lig[i][i2]].val)+" o:"+str(redeN[lig[i][i2]].oco)+" } ")
    arq.close()
    

    P("processando a deducao")
    #BUSCAR APRENDIZADO
    #verificado se nao e o primeiro aprendizado    
    if len(hist) > 0:
        
        P("ha historico entao, buscando po memorias")
        # o bit recolhera a sequencia em bloco crescente , aparetir do ulktimo registro
        bit = 1
        P("bit = 1")
        #loop para encontrar todas as possiveis previsoes em varios niveis
        while bit <= len(hist):
            P("!" + str(bit) +"<"+str(len(hist)) + "!")
            #buscando os ultimos digitos da sequencia
            ultbit=hist[len(hist)-bit:len(hist)]
            P("sequencia de analise:" + ultbit)
            # VERIFICANDO se ja tem um conhecimento para ele
            P("verificando a existencia em LIG")
            if ultbit in lig:
                P("existe!")
                #anotando o link das possiveis previsoes baseada nesta sequencia
                ChavePrev[str(len(prev))] = ultbit
                prev.append(lig[ultbit])
                P("!previsao anotada prev[?] = lig[ultibit] !\n prev[n?][n?] = objeto tipo *neuro*")
            bit += 1
            P("bit =" + str(bit))
        # ENTENDENDO O APRENDIZADO ENCONTRADO
        # lendo as previsoes e analizando as probabilidades

    P("analizando previsoes para encottrar a mais coerente")
    if len(prev) != 0:
        P("!- ha uma lista de previsoes de pelo menos um digito -!")
        arq_prev = open('prev.txt','w')
        for i in range (0,len(prev),1):
            P("precorrendo vetor prev: i =" + str(i))
            # verificando referencias
            for i2 in range (0,len(prev[i]),1):
                arq_prev.write("prev["+str(i)+"] = { v:" + str(redeN[prev[i][i2]].val) + " , o:" + str(redeN[prev[i][i2]].oco) + "}\n")
                P("percorrendo vetor prev["+str(i)+"]: i2 = "+str(i2))
                # encontrando valores pela referencia
                #   -brevemente criar previsao de referencia logica em outros neuronios-
                # Adcionando valor a lista e somando a outras previsoes
                P("adcionanto valores a lista score com indice string um padrao de resposta")
                if redeN[prev[i][i2]].val in score:
                    score[redeN[prev[i][i2]].val] += redeN[prev[i][i2]].oco
                else:
                    score[redeN[prev[i][i2]].val] = redeN[prev[i][i2]].oco
        #calculando maior probabilidade
        pontos = 0
        for i in score.keys():
            pontos += score[i]
            print( str(score[i]) + " pontos para " + str(i))
            arq_prev.write(str(score[i]) + " pontos para " + str(i))
        print("pontos acomulados: " + str(pontos))
        arq_prev.write("score: " + str(pontos) )
        for i in sorted(score.keys(),reverse=True):
            print (str((score[i] * 100) / pontos)+"% para '" + i + "'")         
            previC = i
        arq_prev.close()
    print("previsao: " + previC)    
    #resultado
def SeqProg(): #opções pré programadas de entradas
    print("escolha uma opção:\n")
    print("1 - 1,0\n")
    print("2 - 0,1\n")
    print("3 - 1,1,0\n")
    print("4 - 0,0,1\n")
    print("5 - 0,1,0\n")
    print("6 - 1,0,1\n")
    metodo = int(input())
    print("quantas vezes ele deve repetir\n")
    repetir = int(input())
    
    if metodo == 1:
        for i in range (0,repetir,1):
            Pense("1")
            Pense("0")
    elif metodo == 2:
        for i in range (0,repetir,1):
            Pense("0")
            Pense("1")
    elif metodo == 3:
        for i in range (0,repetir,1):
            Pense("1")
            Pense("1")
            Pense("0")
    elif metodo == 4:
        for i in range (0,repetir,1):
            Pense("0")
            Pense("0")
            Pense("1")
    elif metodo == 5:
        for i in range (0,repetir,1):
            Pense("0")
            Pense("1")
            Pense("0")
    elif metodo == 6:
        for i in range (0,repetir,1):
            Pense("1")
            Pense("0")
            Pense("1")
    else:
        print("opção invalida!")
        SeqProg()
    

def start():
    while 1 == 1: #run
        entrada = str(input("digite um valor de entrada '{}' para sequencia programada:"))
        if entrada == "{}":
            SeqProg()
        else:
            Pense(entrada)
        
start()